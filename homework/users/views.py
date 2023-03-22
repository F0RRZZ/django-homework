from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, ListView

from users.models import UserProfile

from users.forms import CustomUserCreationForm, UserProfileForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = (
        reverse_lazy('users:activation_done')
        if not settings.DEBUG
        else reverse_lazy('index:index')
    )

    def form_valid(self, form):
        user = form.save(commit=False)
        if not settings.DEBUG:
            user.is_active = False
            user.save()

            absolute_url = self.request.build_absolute_uri(
                reverse_lazy(
                    'users:activate',
                    args=[user.username],
                )
            )

            send_mail(
                'Подтверждение регистрации',
                f'Для активации аккаунта перейдите по ссылке: {absolute_url}',
                settings.EMAIL,
                [user.email],
                fail_silently=False,
            )
        else:
            user.is_active = True
            user.save()
        return super().form_valid(form)


class ActivateUserView(DetailView):
    model = UserProfile
    template_name = 'users/confirm_email.html'

    def get_object(self, queryset=None):
        user = get_object_or_404(UserProfile, username=self.kwargs['username'])

        if not user.is_active:
            if user.last_login is None:
                if timezone.now() - user.date_joined > timezone.timedelta(
                    hours=12
                ):
                    raise Http404
            else:
                if timezone.now() - user.date_joined > timezone.timedelta(
                    weeks=1
                ):
                    raise Http404
        else:
            raise Http404

        user.is_active = True
        user.save()

        return user


class UserListView(ListView):
    model = UserProfile
    template_name = 'users/user_list.html'

    def get_queryset(self):
        return UserProfile.objects.filter(is_active=True)


@login_required
def activation_done(request):
    template = 'users/activate_link_sends.html'
    return render(request, template)


@login_required
def user_detail(request, pk):
    user = get_object_or_404(UserProfile, id=pk)
    first_name = user.first_name if user.first_name else 'не указано'
    last_name = user.last_name if user.last_name else 'не указано'
    birthday = (
        user.birthday.strftime('%d.%m.%Y') if user.birthday else 'не указано'
    )
    image = user.image if user.image else None
    coffee_count = user.coffee_count
    context = {
        'email': user.email,
        'first_name': first_name,
        'last_name': last_name,
        'birthday': birthday,
        'image': image,
        'coffee_count': coffee_count,
    }
    return render(request, 'users/user_detail.html', context)


@login_required
def profile_view(request):
    profile_form = UserProfileForm(instance=request.user)
    if request.method == 'POST':
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=request.user
        )
        if profile_form.is_valid():
            profile_form.save()
            return redirect('users:profile')
    return render(
        request,
        'users/profile.html',
        {
            'profile_form': profile_form,
            'image': request.user.image,
            'coffee_count': request.user.coffee_count,
        },
    )


@login_required
def drink_coffee(request):
    profile = request.user
    profile.coffee_count += 1
    profile.save()
    return redirect('users:profile')

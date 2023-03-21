from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, ListView

from users.models import UserProfile

from users.forms import CustomUserCreationForm, UserForm, UserProfileForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:activation_done')

    def form_valid(self, form):
        if not settings.DEBUG:
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            UserProfile.objects.create(user=user)

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
        return super().form_valid(form)


class ActivateUserView(DetailView):
    model = UserProfile
    template_name = 'users/confirm_email.html'

    def get_object(self, queryset=None):
        user_profile = get_object_or_404(
            User, username=self.kwargs['username']
        )

        if timezone.now() - user_profile.date_joined > timezone.timedelta(
            hours=12
        ):
            raise Http404

        user_profile.is_active = True
        user_profile.save()

        return user_profile


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'

    def get_queryset(self):
        return User.objects.filter(is_active=True)


@login_required
def activation_done(request):
    template = 'users/activate_link_sends.html'
    return render(request, template)


@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, id=pk)
    profile = user.profile
    first_name = user.first_name if user.first_name else 'не указано'
    last_name = user.last_name if user.last_name else 'не указано'
    birthday = (
        profile.birthday.strftime('%d.%m.%Y')
        if profile.birthday
        else 'не указано'
    )
    image = profile.image if profile.image else None
    coffee_count = profile.coffee_count
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
    user_form = UserForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('users:profile')
    return render(
        request,
        'users/profile.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
            'image': request.user.profile.image,
            'coffee_count': request.user.profile.coffee_count,
        },
    )


@login_required
def drink_coffee(request):
    profile = request.user.profile
    profile.coffee_count += 1
    profile.save()
    return redirect('users:profile')

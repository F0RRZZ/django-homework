from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

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
        if not settings.USERS_AUTOACTIVATE:
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

        if user.last_login is None:
            if timezone.now() - user.date_joined > timezone.timedelta(
                hours=12
            ):
                raise Http404
        else:
            if timezone.now() - user.date_joined > timezone.timedelta(weeks=1):
                raise Http404

        user.is_active = True
        user.save()

        return user


class UserListView(ListView):
    model = UserProfile
    template_name = 'users/user_list.html'

    def get_queryset(self):
        return UserProfile.objects.filter(is_active=True)


class ActivationDoneView(TemplateView, LoginRequiredMixin):
    template_name = 'users/activate_link_sends.html'


class UserDetailView(DetailView, LoginRequiredMixin):
    template_name = 'users/user_detail.html'
    queryset = UserProfile.objects.all()
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        first_name = user.first_name if user.first_name else 'не указано'
        last_name = user.last_name if user.last_name else 'не указано'
        email = user.email if user.email else 'не указано'
        birthday = user.birthday if user.birthday else 'не указано'
        image = user.image if user.image else 'не указано'
        coffee_count = user.coffee_count if user.coffee_count else 'не указано'
        context.update(
            {
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'birthday': birthday,
                'image': image,
                'coffee_count': coffee_count,
            }
        )
        return context


class ProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = self.request.user.image
        context['coffee_count'] = self.request.user.coffee_count
        return context


class DrinkCoffeeView(TemplateView, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        profile = request.user
        profile.coffee_count += 1
        profile.save()
        return redirect('users:profile')
        # При указании success_url вылетала ошибка
        return redirect('users:profile')

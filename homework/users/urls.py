import django.contrib.auth.views
import django.urls

from users import views

app_name = 'users'
urlpatterns = [
    django.urls.path(
        'login/',
        django.contrib.auth.views.LoginView.as_view(
            template_name='registration/login.html',
        ),
        name='login',
    ),
    django.urls.path(
        'logout/',
        django.contrib.auth.views.LogoutView.as_view(
            template_name='registration/logout.html',
        ),
        name='logout',
    ),
    django.urls.path(
        'password_change/',
        django.contrib.auth.views.PasswordChangeView.as_view(
            template_name='registration/password_change.html',
        ),
        name='password_change',
    ),
    django.urls.path(
        'password_change/done',
        django.contrib.auth.views.PasswordChangeDoneView.as_view(
            template_name='registration/password_change_done.html',
        ),
        name='password_change_done',
    ),
    django.urls.path(
        'password_reset/',
        django.contrib.auth.views.PasswordResetView.as_view(
            template_name='registration/password_reset.html',
        ),
        name='password_reset',
    ),
    django.urls.path(
        'password_reset/done',
        django.contrib.auth.views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    django.urls.path(
        'reset/<uidb64>/<token>',
        django.contrib.auth.views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
        ),
        name='password_reset_confirm',
    ),
    django.urls.path(
        'reset/done',
        django.contrib.auth.views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
    django.urls.path('signup/', views.SignUpView.as_view(), name='signup'),
    django.urls.path(
        'activate/<str:username>/',
        views.ActivateUserView.as_view(),
        name='activate',
    ),
    django.urls.path(
        'activate/done',
        views.ActivationDoneView.as_view(),
        name='activation_done',
    ),
    django.urls.path(
        'user_list/', views.UserListView.as_view(), name='user_list'
    ),
    django.urls.path(
        'user_detail/<int:pk>/',
        views.UserDetailView.as_view(),
        name='user_detail',
    ),
    django.urls.path('profile/', views.ProfileView.as_view(), name='profile'),
    django.urls.path(
        'drink_coffee/', views.DrinkCoffeeView.as_view(), name='drink_coffee'
    ),
]

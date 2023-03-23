from http import HTTPStatus

from django.conf import settings
from django.db.utils import IntegrityError
from django.shortcuts import reverse
from django.test import Client, TestCase, override_settings
from django.utils import timezone
from unittest.mock import patch

from users.forms import UserProfile


class SignUpTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse('users:signup')
        self.test_user_data = {
            'username': 'testuser',
            'email': 'test@user.com',
            'password1': 'fF5bo0zTVN',
            'password2': 'fF5bo0zTVN',
        }

    @override_settings(USERS_AUTOACTIVATE=True)
    def test_signup_with_debug_true(self):
        response = Client().post(self.url, data=self.test_user_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        user = UserProfile.objects.get(
            username=self.test_user_data.get('username')
        )
        self.assertTrue(user.is_active)

    @override_settings(USERS_AUTOACTIVATE=False)
    def test_signup_with_debug_false(self):
        response = Client().post(self.url, data=self.test_user_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        user = UserProfile.objects.get(
            username=self.test_user_data.get('username')
        )
        self.assertFalse(user.is_active)

    @override_settings(USERS_AUTOACTIVATE=False)
    def test_activate_user_within_12_hours(self):
        Client().post(self.url, data=self.test_user_data)
        activation_url = reverse(
            'users:activate', args=[self.test_user_data['username']]
        )
        activation_response = Client().get(activation_url)
        self.assertEqual(activation_response.status_code, HTTPStatus.OK)
        user = UserProfile.objects.get(
            username=self.test_user_data['username']
        )
        self.assertTrue(user.is_active)

    @override_settings(USERS_AUTOACTIVATE=False)
    def test_activate_user_after_12_hours(self):
        Client().post(self.url, data=self.test_user_data)
        activation_url = reverse(
            'users:activate', args=[self.test_user_data['username']]
        )
        with patch.object(
            timezone,
            'now',
            return_value=timezone.now() + timezone.timedelta(hours=13),
        ):
            activation_response = Client().get(activation_url)
            self.assertEqual(
                activation_response.status_code, HTTPStatus.NOT_FOUND
            )
            user = UserProfile.objects.get(
                username=self.test_user_data['username']
            )
            self.assertFalse(user.is_active)

    @override_settings(USERS_AUTOACTIVATE=True)
    def test_yandex_email_formatting(self):
        Client().post(
            self.url,
            {
                'username': 'test',
                'email': 'yandex.test@ya.ru',
                'password1': 'fF5bo0zTVN',
                'password2': 'fF5bo0zTVN',
            },
        )
        user = UserProfile.objects.get(username='test')
        self.assertEqual(user.normalized_email, 'yandex-test@yandex.ru')

    @override_settings(USERS_AUTOACTIVATE=True)
    def test_google_email_formatting(self):
        Client().post(
            self.url,
            {
                'username': 'test',
                'email': 'google.test+test@gmail.com',
                'password1': 'fF5bo0zTVN',
                'password2': 'fF5bo0zTVN',
            },
        )
        user = UserProfile.objects.get(username='test')
        self.assertEqual(user.normalized_email, 'googletest@gmail.com')

    @override_settings(USERS_AUTOACTIVATE=True)
    def test_with_similar_emails(self):
        Client().post(
            self.url,
            {
                'username': 'test1',
                'email': 'yandex.test@ya.ru',
                'password1': 'fF5bo0zTVN',
                'password2': 'fF5bo0zTVN',
            },
        )
        with self.assertRaises(IntegrityError):
            Client().post(
                self.url,
                {
                    'username': 'test2',
                    'email': 'yandex-test@yandex.ru',
                    'password1': 'fF5bo0zTVN',
                    'password2': 'fF5bo0zTVN',
                },
            )

    @override_settings(USERS_AUTOACTIVATE=False)
    def test_failed_authorization_for_the_maximum_number_of_attempts(self):
        Client().post(
            self.url,
            self.test_user_data
        )
        activation_url = reverse(
            'users:activate', args=[self.test_user_data['username']]
        )
        Client().get(activation_url)
        user = UserProfile.objects.get(
            username=self.test_user_data['username']
        )
        self.assertTrue(user.is_active)
        Client().get(reverse('users:logout'))
        for _ in range(settings.MAX_FAILED_ATTEMPTS):
            Client().post(
                reverse('users:login'),
                {
                    'username': 'testuser',
                    'password': 'invalid',
                }
            )
        user = UserProfile.objects.get(
            username=self.test_user_data['username']
        )
        self.assertFalse(user.is_active)

    @override_settings(USERS_AUTOACTIVATE=False)
    def test_failed_authorization_activation_link_within_one_week(self):
        Client().post(
            self.url,
            self.test_user_data
        )
        activation_url = reverse(
            'users:activate', args=[self.test_user_data['username']]
        )
        Client().get(activation_url)
        Client().get(reverse('users:logout'))
        for _ in range(settings.MAX_FAILED_ATTEMPTS):
            Client().post(
                reverse('users:login'),
                {
                    'username': 'testuser',
                    'password': 'invalid',
                }
            )
        activation_url = reverse(
            'users:activate', args=[self.test_user_data['username']]
        )
        Client().get(activation_url)
        user = UserProfile.objects.get(
            username=self.test_user_data['username']
        )
        self.assertTrue(user.is_active)
        response = Client().post(
            self.url,
            self.test_user_data
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @override_settings(USERS_AUTOACTIVATE=False)
    def test_failed_authorization_activation_link_after_one_week(self):
        Client().post(
            self.url,
            self.test_user_data
        )
        activation_url = reverse(
            'users:activate', args=[self.test_user_data['username']]
        )
        Client().get(activation_url)
        Client().get(reverse('users:logout'))
        for _ in range(settings.MAX_FAILED_ATTEMPTS):
            Client().post(
                reverse('users:login'),
                {
                    'username': 'testuser',
                    'password': 'invalid',
                }
            )
        activation_url = reverse(
            'users:activate', args=[self.test_user_data['username']]
        )
        with patch.object(
                timezone,
                'now',
                return_value=timezone.now() + timezone.timedelta(
                    weeks=1, hours=1
                ),
        ):
            Client().get(activation_url)
            user = UserProfile.objects.get(
                username=self.test_user_data['username']
            )
            self.assertFalse(user.is_active)

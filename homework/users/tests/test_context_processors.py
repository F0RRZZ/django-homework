import datetime

from django.shortcuts import reverse
from django.test import Client, TestCase
import freezegun
import parameterized.parameterized

from users.forms import UserProfile


class BirthdayContextTests(TestCase):
    def setUp(self):
        self.base_url = reverse('homepage:index')
        self.test_user_data = {
            'username': 'testuser',
            'email': 'test@user.com',
            'password1': 'fF5bo0zTVN',
            'password2': 'fF5bo0zTVN',
        }
        users_data = [
            [
                datetime.datetime(1995, 10, 10, tzinfo=datetime.timezone.utc),
                True,
            ],
            [
                datetime.datetime(2009, 11, 11, tzinfo=datetime.timezone.utc),
                True,
            ],
            [
                datetime.datetime(2006, 10, 10, tzinfo=datetime.timezone.utc),
                True,
            ],
            [
                datetime.datetime(2004, 11, 11, tzinfo=datetime.timezone.utc),
                True,
            ],
            [
                datetime.datetime(2003, 11, 11, tzinfo=datetime.timezone.utc),
                True,
            ],
            [
                datetime.datetime(1990, 10, 10, tzinfo=datetime.timezone.utc),
                False,
            ],
        ]
        for i in range(1, len(users_data) + 1):
            user = UserProfile.objects.create(
                first_name=f'f_name{i}',
                last_name=f'l_name{i}',
                username=f'user{i}',
                email=f'address{i}@example.com',
                birthday=users_data[i - 1][0],
                is_active=users_data[i - 1][1],
            )
            user.set_password(f'very_strong{i}')
        super().setUp()

    @parameterized.parameterized.expand(
        [
            [
                reverse('homepage:index'),
            ],
            [
                reverse('catalog:item-list'),
            ],
            [
                reverse('catalog:item-list'),
            ],
            [
                reverse('catalog:new-items'),
            ],
            [
                reverse('about:description'),
            ],
        ]
    )
    def test_user_list_exists(self, url):
        response = Client().get(url)
        context = response.context
        self.assertIn('birthday_users', context.keys())

    @parameterized.parameterized.expand(
        [
            [10, 10, 2],
            [11, 11, 3],
            [12, 12, 0],
        ]
    )
    def test_user_list_count(self, month, day, user_count):
        with freezegun.freeze_time(
            datetime.datetime(
                2020, month, day, hour=1, tzinfo=datetime.timezone.utc
            ),
        ):
            response = Client().get(self.base_url)
            user_list = response.context['birthday_users']
            self.assertEqual(len(user_list), user_count)

    def test_user_element_keys(self):
        with freezegun.freeze_time(
            datetime.datetime(
                2020, 10, 10, hour=1, tzinfo=datetime.timezone.utc
            ),
        ):
            response = Client().get(self.base_url)
            user_dict_keys = response.context['birthday_users'][0].keys()
            self.assertIn('first_name', user_dict_keys)
            self.assertIn('last_name', user_dict_keys)
            self.assertIn('email', user_dict_keys)

    def test_user_element_data(self):
        with freezegun.freeze_time(
            datetime.datetime(2020, 10, 10, tzinfo=datetime.timezone.utc),
        ):
            response = Client().get(self.base_url)
            user_dict = response.context['birthday_users'][0]
            self.assertEqual(user_dict['first_name'], 'f_name1')
            self.assertEqual(user_dict['last_name'], 'l_name1')
            self.assertEqual(user_dict['email'], 'address1@example.com')

from http import HTTPStatus

from django.test import Client, TestCase, override_settings

from homework.middleware.russian_words_reverser import reverse_russian_words


class CustomMiddlewareTests(TestCase):
    def test_is_middleware_correctly_working(self):
        with override_settings(
            RUSSIAN_WORDS_REVERSING_MIDDLEWARE_ENABLED=False
        ):
            client = Client()
            response = client.get('/')
            self.assertEqual(response.status_code, HTTPStatus.OK)
            original_text = response.content.decode('utf-8')
            reversed_text = original_text
            for _ in range(20):
                response = client.get('/')
                text = response.content.decode('utf-8')
                if text != original_text:
                    reversed_text = text
                    break
            self.assertEquals(original_text, reversed_text)

    def test_is_content_reversing(self):
        with override_settings(
            RUSSIAN_WORDS_REVERSING_MIDDLEWARE_ENABLED=True
        ):
            client = Client()
            response = client.get('/')
            original_text = response.content.decode('utf-8')
            reversed_text = ''
            for _ in range(20):
                response = client.get('/')
                text = response.content.decode('utf-8')
                if text != original_text:
                    reversed_text = reverse_russian_words(text)
                    break
            self.assertEqual(original_text, reversed_text)

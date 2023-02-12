import environ
from django.test import Client, TestCase

env = environ.Env(CUSTOM_MIDDLEWARE_ENABLED=(bool, False))
middleware_enabled = env('CUSTOM_MIDDLEWARE_ENABLED')


class CustomMiddlewareTests(TestCase):
    def test_is_content_reversing(self):
        client = Client()
        response = client.get('/')
        first_response_text = (
            response.content.decode('utf-8')
            .replace('<body>', '')
            .replace('</body>', '')
        )
        for _ in range(9):
            response = client.get('/')
        tenth_response_text = (
            response.content.decode('utf-8')
            .replace('<body>', '')
            .replace('</body>', '')
        )
        if middleware_enabled:
            self.assertEqual(first_response_text, tenth_response_text[::-1])
        else:
            self.assertEqual(first_response_text, tenth_response_text)

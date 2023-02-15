from django.conf import settings
from django.test import Client, TestCase

middleware_enabled = settings.WORDS_REVERSING_MIDDLEWARE_ENABLED


class CustomMiddlewareTests(TestCase):
    def test_is_content_reversing(self):
        client = Client()
        response = client.get('/')
        first_response_text = response.content.decode('utf-8')
        for _ in range(9):
            response = client.get('/')
        tenth_response_text = response.content.decode('utf-8')
        if middleware_enabled:
            self.assertEqual(first_response_text, tenth_response_text[::-1])
        else:
            self.assertEqual(first_response_text, tenth_response_text)

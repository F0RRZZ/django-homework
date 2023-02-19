from http import HTTPStatus

from django.test import TestCase, override_settings
from homepage import views


class CustomMiddlewareTests(TestCase):
    @override_settings(RUSSIAN_WORDS_REVERSING_MIDDLEWARE_ENABLED=False)
    def test_reverse_russian_words_disabled(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        original_text = response.content.decode('utf-8')
        reversed_text = original_text
        for _ in range(10):
            response = self.client.get('/')
            text = response.content.decode('utf-8')
            if text != original_text:
                reversed_text = text
                break
        self.assertEquals(original_text, reversed_text)

    @override_settings(RUSSIAN_WORDS_REVERSING_MIDDLEWARE_ENABLED=True)
    def test_reverse_russian_words_enabled(self):
        cases = [
            ('/', '!стр124ок[a]', '!ртс124ко[a]'),
            ('/', '1287!*#&874198274#!', '1287!*#&874198274#!'),
            ('/', 'hello', 'hello'),
            ('/', ' ', ' '),
            ('/', 'шdшdшdшdшd', 'шdшdшdшdшd'),
            ('/', 'ГлаВнаЯ', 'ЯанВалГ'),
            ('/', 'helloпривет', 'helloтевирп'),
        ]
        for case in cases:
            views.homepage_title = case[1]
            result = []
            for _ in range(10):
                response = self.client.get(case[0])
                result.append(response.content.decode('utf-8'))
            self.assertIn(
                case[2],
                result,
                f'\nRussian words reversing middleware'
                f' did not give the correct result'
                f'(case: {case[1]}; expected: {case[2]})',
            )

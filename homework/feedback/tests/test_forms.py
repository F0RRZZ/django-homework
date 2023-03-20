from django.test import TestCase

import feedback.forms


class FormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = feedback.forms.FeedbackForm()

    def test_text_label(self):
        text_label = FormTests.form.fields['text'].label
        self.assertEqual(text_label, 'Текст')

    def test_email_label(self):
        email_label = FormTests.form.fields['email'].label
        self.assertEqual(email_label, 'Ваша почта')

    def test_text_help_text(self):
        text_help_text = FormTests.form.fields['text'].help_text
        self.assertEqual(text_help_text, 'содержание письма')

    def test_email_help_text(self):
        email_help_text = FormTests.form.fields['email'].help_text
        self.assertEqual(
            email_help_text, 'введите почту, на которую будет отправлен ответ'
        )

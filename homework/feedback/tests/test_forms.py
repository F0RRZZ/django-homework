import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse

import feedback.models
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

    def test_create_feedback(self):
        feedbacks_count = feedback.models.Feedback.objects.count()
        form_data = {'text': 'text', 'email': 'ex@ex.com'}
        Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True,
        )
        self.assertEqual(
            feedback.models.Feedback.objects.count(), feedbacks_count + 1
        )
        self.assertTrue(
            feedback.models.Feedback.objects.filter(text='text').exists()
        )

    def test_redirect(self):
        form_data = {'text': 'text', 'email': 'ex@ex.com'}
        response = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True,
        )
        self.assertRedirects(response, reverse('feedback:success'))

    def test_file_upload(self):
        with open('test_file.txt', 'w') as f:
            f.write('test')
        with open('test_file.txt', 'rb') as f:
            form_data = {
                'text': 'text',
                'email': 'ex@ex.com',
                'files': SimpleUploadedFile(f.name, f.read()),
            }
            Client().post(
                reverse('feedback:feedback'),
                data=form_data,
                follow=True,
            )
            self.assertTrue(os.path.exists('uploads/1/test_file.txt'))
        os.remove('uploads/1/test_file.txt')
        os.remove('test_file.txt')
        os.rmdir('uploads/1/')

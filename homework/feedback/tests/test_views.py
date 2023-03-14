from django.test import Client, TestCase
from django.urls import reverse


class FeedbackViewTests(TestCase):
    def test_feedback_page_context(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('forms', response.context)

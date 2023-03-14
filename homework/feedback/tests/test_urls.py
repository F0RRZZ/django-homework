from http import HTTPStatus

from django.test import Client, TestCase


class FeedbackPageTests(TestCase):
    def test_feedback_endpoint(self):
        response = Client().get('/feedback/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            'Error when going to the page "feedback"',
        )

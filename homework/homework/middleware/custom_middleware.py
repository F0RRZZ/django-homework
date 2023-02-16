from django.conf import settings
from django.http import HttpResponse

from homework.middleware.russian_words_reverser import reverse_russian_words


class RussianWordsReverseMiddleware:
    def __init__(self, get_response):
        self.counter = 0
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not settings.RUSSIAN_WORDS_REVERSING_MIDDLEWARE_ENABLED:
            return response
        if self.counter != 9:
            self.counter += 1
            return response
        self.counter = 0
        text = response.content.decode('utf-8')
        return HttpResponse(reverse_russian_words(text))

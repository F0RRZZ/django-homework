from django.conf import settings
from django.http import HttpResponse

middleware_enabled = settings.WORDS_REVERSING_MIDDLEWARE_ENABLED


class RussianWordsReverseMiddleware:
    def __init__(self, get_response):
        self.counter = 0
        self.get_response = get_response

    @classmethod
    def reverse_russian_words(cls, text):
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        result, word = '', ''
        for symbol in text:
            if symbol.lower() not in alphabet:
                if word:
                    result += word[::-1]
                    word = ''
                result += symbol
            else:
                word += symbol
        result += word[::-1]
        return result

    def __call__(self, request):
        response = self.get_response(request)
        if not middleware_enabled:
            return response
        if self.counter != 9:
            self.counter += 1
            return response
        self.counter = 0
        text = response.content.decode('utf-8')
        return HttpResponse(self.reverse_russian_words(text))

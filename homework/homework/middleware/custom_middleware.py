import os
from pathlib import Path

import environ
from django.http import HttpResponse

BASE_DIR = Path(__file__).parent.parent.parent

env = environ.Env(CUSTOM_MIDDLEWARE_ENABLED=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
middleware_enabled = env('CUSTOM_MIDDLEWARE_ENABLED')


class CustomMiddleware:
    def __init__(self, get_response):
        self.counter = 0
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not middleware_enabled:
            return response
        if self.counter != 9:
            self.counter += 1
            return response
        self.counter = 0
        text = response.content.decode('utf-8')
        return HttpResponse(text[::-1])

import environ
from django.http import HttpResponse

env = environ.Env(CUSTOM_MIDDLEWARE_ENABLED=(bool, False))
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
        text = (
            response.content.decode('utf-8')
            .replace('<body>', '')
            .replace('</body>', '')
        )
        return HttpResponse(f'<body>{text[::-1]}</body>')

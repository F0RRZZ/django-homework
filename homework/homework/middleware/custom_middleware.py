from django.http import HttpResponse


class CustomMiddleware:
    def __init__(self, get_response):
        self.counter = 0
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if self.counter != 10:
            self.counter += 1
            return response
        self.counter = 0
        text = (
            response.content.decode('utf-8')
            .replace('<body>', '')
            .replace('</body>', '')
        )
        new_response = HttpResponse(f'<body>{text[::-1]}</body>')
        return new_response

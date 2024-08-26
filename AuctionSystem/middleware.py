from django.conf import settings
from django.http import JsonResponse

class AdminSecretMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/'):
            api_secret = request.headers.get('Authorization')
            if api_secret != f'ApiKey {settings.STATIC_API_SECRET}':
                return JsonResponse({'detail': 'Unauthorized'}, status=401)

        response = self.get_response(request)
        return response

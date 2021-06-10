from django.http import JsonResponse


def error404(request, exception=None) -> JsonResponse:
    return JsonResponse({
        'detail': "Resource not found.",
    }, status=404)

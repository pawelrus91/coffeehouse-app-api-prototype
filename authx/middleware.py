from django.utils.timezone import now
from .models import CustomUser


class SetLastLogin:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            user = CustomUser.objects.get(id=request.user.id)
            user.last_login = now()
            user.save()

        response = self.get_response(request)
        return response

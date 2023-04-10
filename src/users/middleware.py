import logging
from typing import Callable

from django.conf import settings
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from ninja_jwt.tokens import RefreshToken

from users.constants import DEV_USER_EMAIL
from users.models import User

logger = logging.getLogger(__name__)


class DevUserAutoLoginMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        if not settings.DEBUG:
            return self.get_response(request)

        dev_user_jwt = getattr(settings, "DEV_USER_JWT", "")

        if not dev_user_jwt:
            logger.warning("'DEV_USER_JWT' env variable not set, creating token afresh")

            try:
                user = User.objects.get(email=DEV_USER_EMAIL)
            except User.DoesNotExist:
                logger.warning(
                    "Dev user %s not found, auto login failed" % DEV_USER_EMAIL
                )
            else:
                refresh = RefreshToken.for_user(user)
                dev_user_jwt = str(refresh.access_token)

        if dev_user_jwt:
            logger.warning("Using dev user %s JWT" % DEV_USER_EMAIL)
            request.META["HTTP_AUTHORIZATION"] = f"Bearer {dev_user_jwt}"

        return self.get_response(request)

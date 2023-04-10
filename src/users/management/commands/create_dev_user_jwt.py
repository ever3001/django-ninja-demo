from datetime import timedelta
from typing import Any

from django.core.management.base import BaseCommand
from ninja_jwt.tokens import AccessToken, RefreshToken

from users.constants import DEV_USER_EMAIL
from users.models import User


class ExtremelyLongLivedAccessToken(AccessToken):
    lifetime: timedelta = timedelta(days=365 * 5)


class CustomRefreshToken(RefreshToken):
    access_token_class = ExtremelyLongLivedAccessToken


class Command(BaseCommand):
    help = "Generate development user JWT for auto login."

    def handle(self, *args: Any, **options: Any) -> None:
        user = User.objects.get(email=DEV_USER_EMAIL)
        refresh = CustomRefreshToken.for_user(user)

        self.stdout.write(str(refresh.access_token))

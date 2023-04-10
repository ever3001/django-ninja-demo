from datetime import date
from typing import Any

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from users.constants import DEV_USER_EMAIL
from users.models import User
from users.tests.factories import MaleProfileFactory, MaleUserFactory


class Command(BaseCommand):
    help = "Create development user if it does not exist."

    def handle(self, *args: Any, **options: Any) -> None:
        if not User.objects.filter(email=DEV_USER_EMAIL).exists():
            user = MaleUserFactory(email=DEV_USER_EMAIL, password=make_password("pwd"))
            MaleProfileFactory(user=user, birth_date=date.fromisoformat("1995-05-05"))

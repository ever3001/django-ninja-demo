from typing import Any

from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Create superuser if it does not exist."

    def handle(self, *args: Any, **options: Any) -> None:
        if not User.objects.filter(email="admin@myapp.com").exists():
            User.objects.create_superuser("admin@myapp.com", "passw0rd")

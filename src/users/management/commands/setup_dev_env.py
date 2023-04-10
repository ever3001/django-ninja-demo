from typing import Any

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Setup dev env."

    def handle(self, *args: Any, **options: Any) -> None:
        call_command("migrate")
        call_command("loaddata", "/app/src/users/fixtures/users.json")

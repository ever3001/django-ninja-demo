from typing import Any

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection
from django.test.utils import setup_test_environment, teardown_test_environment

from users.tests.factories import FemaleProfileFactory, MaleProfileFactory


class Command(BaseCommand):
    help = "Create users fixture JSON file."

    def handle(self, *args: Any, **options: Any) -> None:
        setup_test_environment()
        db = connection.creation.create_test_db(autoclobber=True, serialize=False)

        try:
            call_command("create_admin_user")
            call_command("create_dev_user")

            for _ in range(25):
                MaleProfileFactory()
                FemaleProfileFactory()

            with open("/app/src/users/fixtures/users.json", "w+") as fixture_file:
                call_command(
                    "dumpdata",
                    "--format=json",
                    "--indent=4",
                    "users",
                    stdout=fixture_file,
                )
        except Exception as exc:  # noqa
            self.stderr.write(f"Failed creating users fixture, reason {exc}")
        finally:
            connection.creation.destroy_test_db(db)
            teardown_test_environment()

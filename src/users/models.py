import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


class User(AbstractUser):
    # https://testdriven.io/blog/django-custom-user-model/
    username = None  # type: ignore
    email = models.EmailField("email address", unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True)

    objects = UserManager()  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email

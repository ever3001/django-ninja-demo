import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from myapp.models import TimeStampedModel
from users.managers import UserManager


class User(AbstractUser):
    # https://testdriven.io/blog/django-custom-user-model/

    username = None  # type: ignore
    email = models.EmailField("email address", unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True)

    viewed_profiles = models.ManyToManyField(
        "self", through="ProfileView", related_name="viewed_by", symmetrical=False
    )
    blocked_users = models.ManyToManyField(
        "self", through="BlockedUser", related_name="blocked_by", symmetrical=False
    )

    objects = UserManager()  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email


class ProfileView(models.Model):
    user = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)
    viewer = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


class BlockedUser(models.Model):
    user = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)
    blocked = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    bio = models.TextField(max_length=500)
    birth_date = models.DateField(db_index=True)

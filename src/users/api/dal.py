from __future__ import annotations

from uuid import UUID

from django.db.models import F, QuerySet, Value
from django.utils import timezone

from users.models import User


def _users_queryset(user: User) -> QuerySet[User]:
    return (
        User.objects.annotate(
            age=(Value(timezone.now().today().year) - F("profile__birth_date__year"))
        ).exclude(profile__isnull=True)
        # .exclude(blocked_users=user.id)  # TODO
    )


def get_users(user: User) -> QuerySet[User]:
    return _users_queryset(user).exclude(id=user.id).order_by("id")


async def get_user_or_none(user: User, uuid: UUID) -> User | None:
    return await _users_queryset(user).filter(uuid=uuid).afirst()

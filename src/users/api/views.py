from __future__ import annotations

from http import HTTPStatus
from uuid import UUID

from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _
from ninja.errors import HttpError
from ninja_extra import Router
from ninja_jwt.authentication import AsyncJWTAuth

from users.api.dal import get_user_or_none, get_users
from users.api.schemas import HttpErrorSchema, UserSchema
from users.models import ProfileView, User
from users.types import Request

router = Router(auth=AsyncJWTAuth())


@router.get(
    "/",
    response={
        HTTPStatus.OK: list[UserSchema],
    },
)
async def user_list(request: Request) -> QuerySet[User]:
    assert isinstance(request.user, User)
    return get_users(request.user)


@router.get(
    "/{uuid}/",
    response={
        HTTPStatus.OK: UserSchema,
        HTTPStatus.NOT_FOUND: HttpErrorSchema,
    },
)
async def user_detail(request: Request, uuid: UUID) -> User:
    if user := await get_user_or_none(request.user, uuid=uuid):
        await ProfileView.objects.acreate(user=user, viewer=request.user)
        return user

    raise HttpError(HTTPStatus.NOT_FOUND, _("User not found"))

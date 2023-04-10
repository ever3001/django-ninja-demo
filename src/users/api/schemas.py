from ninja import ModelSchema, Schema
from pydantic import validator

from users.models import Profile, User


class ProfileSchema(ModelSchema):
    age: int

    class Config:
        model = Profile
        model_fields = [
            "bio",
        ]


class UserSchema(ModelSchema):
    profile: ProfileSchema

    class Config:
        model = User
        model_fields = ["first_name", "last_name"]

    @validator("profile", pre=True, allow_reuse=True)
    def pass_age(cls, profile: Profile) -> Profile:
        # `.age` comes from an annotation, hence ignoring type checks.
        profile.age = profile.user.age  # type: ignore
        return profile


class HttpErrorSchema(Schema):
    message: str

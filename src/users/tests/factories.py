from datetime import date
from random import randint, sample

import factory
from django.contrib.auth.hashers import make_password

from users.models import Profile, User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.LazyAttribute(
        lambda user: make_password(f"{user.first_name}{user.last_name}_pwd")
    )
    email = factory.LazyAttributeSequence(
        lambda user, n: f"{user.first_name}{user.last_name}{n}@example.com".lower()
    )


class MaleUserFactory(UserFactory):
    first_name = factory.Faker("first_name_male")
    last_name = factory.Faker("last_name_male")


class FemaleUserFactory(UserFactory):
    first_name = factory.Faker("first_name_female")
    last_name = factory.Faker("last_name_female")


def random_sublist(values: list) -> list:
    return sample(values, randint(1, len(values)))


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)

    bio = factory.Faker("pystr")
    birth_date = factory.Faker(
        "date_between_dates",
        date_start=date.fromisoformat("1980-01-01"),
        date_end=date.fromisoformat("2000-12-31"),
    )


class MaleProfileFactory(ProfileFactory):
    user = factory.SubFactory(MaleUserFactory)


class FemaleProfileFactory(ProfileFactory):
    user = factory.SubFactory(FemaleUserFactory)

import uuid
from http import HTTPStatus

from asgiref.sync import sync_to_async
from django.test import TestCase
from django.urls import reverse

from users.models import ProfileView
from users.tests.api.utils import client_factory
from users.tests.factories import FemaleProfileFactory, MaleProfileFactory


class UsersTestCase(TestCase):
    url = reverse("api-1.0.0:user_list")

    def setUp(self):
        self.profile = MaleProfileFactory()
        self.user = self.profile.user

        self.client = client_factory(self.user)

    async def test_user_list(self):
        await sync_to_async(FemaleProfileFactory)()

        response = await self.client.get(self.url)
        assert response.status_code == HTTPStatus.OK
        assert len(response.json()) == 1

    async def test_user_detail(self):
        them = await sync_to_async(FemaleProfileFactory)()

        response = await self.client.get(f"{self.url}{them.user.uuid}/")
        assert response.status_code == HTTPStatus.OK

        profile_view = await (
            ProfileView.objects.filter(viewer=self.user).values("user__uuid").afirst()
        )
        assert profile_view["user__uuid"] == them.user.uuid

    async def test_user_detail_not_found(self):
        response = await self.client.get(f"{self.url}{uuid.uuid4()}/")
        assert response.status_code == HTTPStatus.NOT_FOUND

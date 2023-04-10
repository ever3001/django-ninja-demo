from django.test import AsyncClient
from ninja_jwt.tokens import RefreshToken


class AuthAsyncClient(AsyncClient):
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    def request(self, **request):
        if self.user:
            refresh = RefreshToken.for_user(self.user)
            request["headers"].append(
                (b"authorization", f"Bearer {refresh.access_token}".encode())
            )

        return super().request(**request)


def client_factory(user=None):
    client = AuthAsyncClient()

    if user:
        client.user = user

    return client

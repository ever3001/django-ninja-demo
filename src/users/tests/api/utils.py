from django.test import AsyncClient


class AuthAsyncClient(AsyncClient):
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value


def client_factory(user=None):
    client = AuthAsyncClient()

    if user:
        client.user = user

    return client

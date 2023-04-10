from django.http.request import HttpRequest

from users.models import User


class Request(HttpRequest):
    auth: User

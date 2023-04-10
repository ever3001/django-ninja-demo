from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from users.api.views import router as users_router

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

api.add_router("/users/", users_router, tags=["users"])

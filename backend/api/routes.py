from fastapi import APIRouter
from api.views import home_view

api_router = APIRouter()

api_router.add_api_route("/travel/recommmendations", home_view.post, methods=["POST"])
api_router.add_api_route("/", home_view.get, methods=["GET"])

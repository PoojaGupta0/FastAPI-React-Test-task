from fastapi import APIRouter

from backend.api.views import home_view

api_router = APIRouter()

api_router.add_api_route("/travel/recomendations", home_view.get, methods=["GET"])

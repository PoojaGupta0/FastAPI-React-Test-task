import time
import pytest

from fastapi.testclient import TestClient
from unittest.mock import patch

from backend.main import app

client = TestClient(app)


class TestHomeView:
    @pytest.mark.parametrize(
        "country, season", [("UK", "summer"), ("Canada", "winter")]
    )
    def test_get_recommendations_success(self, country, season):
        response = client.get(
            f"/api/travel/recomendations?country={country}&season={season}"
        )
        assert response.status_code == 200
        assert "recommendations" in response.json()
        time.sleep(3)

    def test_get_recommendations_invalid_input(self):
        response = client.get("/api/travel/recomendations?country=USA&season=autumn")
        assert (
            response.status_code == 400
        )  # Expecting a 400 status code for invalid input
        assert "detail" in response.json()

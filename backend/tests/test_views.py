
import pytest, openai
from fastapi.testclient import TestClient
from unittest.mock import patch
from backend.main import app
import time

client = TestClient(app)

class TestHomeView:

    @pytest.mark.parametrize("country, season", [("UK", "summer"), ("Canada", "winter")])
    def test_get_recommendations_success(self, country, season):
        response = client.get(f"/api/travel/recomendations?country={country}&season={season}")
        assert response.status_code == 200
        assert "recommendations" in response.json()
        time.sleep(3)

    def test_get_recommendations_invalid_input(self):
        response = client.get("/api/travel/recomendations?country=USA&season=autumn")
        assert response.status_code == 400  # Expecting a 400 status code for invalid input
        assert "detail" in response.json()

    @patch("backend.api.views.openai.Completion.create")
    def test_get_recommendations_rate_limit_exceeded(self, mock_openai_create):
        # Configure the OpenAI API client to raise a RateLimitError
        from openai.error import RateLimitError

        mock_openai_create.side_effect = RateLimitError("Rate limit exceeded")
        # Make the actual API request
        response = client.get("/api/travel/recomendations?country=USA&season=summer")
        print(response.status_code)
        print(response.text)

        # Check that the application correctly handles the RateLimitError
        assert response.status_code == 429
        assert "Rate limit exceeded" in response.text

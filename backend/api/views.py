import os, json, openai

from fastapi import HTTPException, Depends, Query
from pydantic import BaseModel, ValidationError
from utils.utils import remove_numbers_bullet_points
import requests.exceptions

# Your OpenAI API key
openai_api_key = os.environ.get("open_ai_key")


# Define a Pydantic model for query parameters
class QueryParams(BaseModel):
    country: str = Query(
        ..., description="Country name is required", min_length=4, max_length=50
    )
    season: str = Query(
        ..., description="Season is required", min_length=4, max_length=20
    )

class HomeView:
    def get_recommendations(self, country, season):
            # Define the prompt/question
        prompt = f"Three recommended activities for someone traveling to {country} in {season}."

        # Make a request to the OpenAI API
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=50,
                api_key=openai_api_key,  # Use environment variable
            )

            # Extract and format the recommendations from the response
            recommendations = response.choices[0].text.strip().replace("\n", "\n")
            return recommendations

        except openai.error.RateLimitError as e:
            raise HTTPException(status_code=429, detail=f"Rate limit exceeded. Retry after 3 seconds")

        except requests.exceptions.Timeout:
            raise HTTPException(status_code=504, detail=f"Request to OpenAI API timed out. Please try again later.")

        except openai.error.OpenAIError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get(self, query_params: QueryParams = Depends()):
        country = query_params.country
        season = query_params.season

        try:
            recommendations = self.get_recommendations(country, season)
            recommendations = remove_numbers_bullet_points(recommendations)

            return {
                "season": season,
                "country": country.title(),
                "recommendations": recommendations
            }

        except (SyntaxError, ValueError, ValidationError) as e:
            raise HTTPException(status_code=400, detail=str(e))

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# Instantiate HomeView class
home_view = HomeView()
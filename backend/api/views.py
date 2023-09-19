import os, json, openai

from fastapi import HTTPException, Depends, Query
from pydantic import BaseModel, ValidationError

# Your OpenAI API key
api_key = os.environ.get("open_ai_key")


# Define a Pydantic model for query parameters
class QueryParams(BaseModel):
    country: str = Query(
        ..., description="Country name is required", min_length=4, max_length=50
    )
    season: str = Query(
        ..., description="Season is required", min_length=4, max_length=20
    )


class HomeView:
    # @handle_errors
    def get(self, query_params: QueryParams = Depends()):
        # Extract query parameters directly from the validated Pydantic model
        country = query_params.country
        season = query_params.season

        # Check if the season is valid
        valid_seasons = {"fall", "summer", "winter", "spring"}
        if season.lower() not in valid_seasons:
            raise HTTPException(status_code=400, detail="Season is invalid")

        # Define the prompt/question
        prompt = f"Three recommended activities for someone traveling to {country} in {season}."

        try:
            # Make a request to the OpenAI API
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=50,
                api_key=api_key,
            )

            # Extract and format the recommendations from the response
            recommendations = response.choices[0].text.strip().replace("\n", "\n")

            return {
                "season": season,
                "country": country,
                "recommendations": recommendations,
            }
        except SyntaxError as e:
            raise HTTPException(status_code=400, detail=f"Syntax Error: {e}")
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Value Error: {e}")
        except ValidationError as e:
            raise HTTPException(status_code=404, detail=f"Validation Error: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")


home_view = HomeView()

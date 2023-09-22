import os, json, openai
import requests.exceptions

from fastapi import HTTPException, Depends
from pydantic import ValidationError

from backend.api.models import QueryParams
from backend.utils.utils import remove_numbers_bullet_points

# Your OpenAI API key
openai_api_key = os.environ.get("open_ai_key")


class HomeView:
    def get_recommendations(self, country, season):
        """sumary_line

        Keyword arguments:
        argument -- country, season
        Return: Get the travel recommendations from Open AI
        """

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
            raise HTTPException(
                status_code=429, detail=f"Rate limit exceeded. Retry after 3 seconds"
            )

        except requests.exceptions.Timeout:
            raise HTTPException(
                status_code=504,
                detail=f"Request to OpenAI API timed out. Please try again later.",
            )

        except openai.error.OpenAIError as e:
            raise HTTPException(status_code=400, detail=str(e))
        
        # Handle the exceptions
        except (SyntaxError, ValueError, ValidationError) as e:
            raise HTTPException(status_code=400, detail=str(e))

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    def get(self, query_params: QueryParams = Depends()):
        """sumary_line

        Keyword arguments:
        argument -- QueryParams
        Return: Get the recommendations with the expected format
        """

        country = query_params.country
        season = query_params.season
        # Call the get recommendation function for getting the results
        recommendations = self.get_recommendations(country, season)
        # Modified the recommendation to remove numbers, bullets and other things to get result in list
        recommendations = remove_numbers_bullet_points(recommendations) if recommendations else []

        return {
            "season": season,
            "country": country.title(),
            "recommendations": recommendations,
        }


# Instantiate HomeView class
home_view = HomeView()

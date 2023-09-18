import openai, os

# Your OpenAI API key
api_key = os.environ.get("open_ai_key")


class HomeView:
    def __init__(self):
        pass

    def post(self, country, season):
        # Define the prompt/question
        prompt = f" Three Recommend activities for someone traveling to {country} in {season}."

        # Make a request to the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-002",  # Choose the appropriate engine
            prompt=prompt,
            max_tokens=50,  # Adjust the max tokens based on your desired response length
            api_key=api_key,
        )

        # Extract and format the recommendations from the response
        recommendations = response.choices[0].text.strip().replace("\n", "\n")

        return {
            "season": season,
            "country": country,
            "recommendations": recommendations,
        }

    def get(self):
        return "Welcome to Server is running"


home_view = HomeView()

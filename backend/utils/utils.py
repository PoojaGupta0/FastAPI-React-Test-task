import re

def remove_numbers_bullet_points(recommendations):
    # Split the recommendations into lines
    lines = recommendations.split('\n')

    # Join the lines back into a single string without numbers or bullet points
    cleaned_recommendations = '\n'.join(lines)

    return cleaned_recommendations

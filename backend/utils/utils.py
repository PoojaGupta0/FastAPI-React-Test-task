import re

# Custom function to clean up and format a single line
def clean_up_line(line):
    # Remove leading numbers, bullets, and whitespace
    cleaned_line = re.sub(r'^\s*[0-9]+[.)]?\s*•?\s*-?\s*', '', line)
    # Add a full stop at the end if it's not there
    if cleaned_line and not cleaned_line.endswith('.'):
        cleaned_line += '.'
    return cleaned_line.strip()

def remove_numbers_bullet_points(recommendations):
    # Split the string using a regular expression to match numbering and bullets
    lines = recommendations.split('\n')

    # Clean up and filter the lines
    elements = [clean_up_line(line) for line in lines if line.strip()]
    return elements

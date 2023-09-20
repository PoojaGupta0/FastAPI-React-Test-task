def remove_numbers_bullet_points(recommendations):
    # Define regular expressions to match numbers, bullet points, and spaces
    number_pattern = r"^\s*\d+\.\s*"
    bullet_pattern = r"^\s*[-•]\s*"
    space_pattern = r"^\s+"

    # Split the recommendations into lines and remove numbering/bullet points
    lines = recommendations.split('\n')
    cleaned_lines = []

    for line in lines:
        # Remove numbers or bullet points at the beginning of each line
        line = re.sub(number_pattern, '', line)
        line = re.sub(bullet_pattern, '', line)
        # Remove leading spaces
        line = re.sub(space_pattern, '', line)
        
        cleaned_lines.append(line)

    # Join the cleaned lines back into a single string
    cleaned_recommendations = '\n'.join(cleaned_lines)
    
    return cleaned_recommendations

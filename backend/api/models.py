from pydantic import BaseModel, validator
from fastapi import HTTPException, Query


# Define a Pydantic model for query parameters
class QueryParams(BaseModel):
    country: str = Query(
        ...,
        description="Country name is required",
        min_length=2,
        max_length=50,
        pattern="^[A-Za-z]+$",
    )
    season: str = Query(
        ..., description="Season is required", min_length=4, max_length=20
    )

    @validator("season")
    def validate_season(cls, value):
        allowed_seasons = ["summer", "winter", "spring", "fall"]
        if value not in allowed_seasons:
            raise HTTPException(
                400, f"Invalid season. Allowed values: {', '.join(allowed_seasons)}"
            )
        return value

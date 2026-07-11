from pydantic import BaseModel, Field

class PreparednessRequest(BaseModel):
    location: str = Field(..., description="User's city or neighborhood")
    family_size: int = Field(..., ge=1, le=20, description="Number of people in household")
    anxiety_level: str = Field(..., description="Low, Moderate, or High", pattern="^(Low|Moderate|High)$")

class PantryRequest(BaseModel):
    ingredients: str = Field(..., description="Comma-separated list of ingredients available")

class SOSRequest(BaseModel):
    situation: str = Field(..., description="Brief description of the emergency")
    location: str = Field(..., description="Current exact location/address")

class CommuteRequest(BaseModel):
    start_location: str = Field(..., description="Starting point")
    end_location: str = Field(..., description="Destination")

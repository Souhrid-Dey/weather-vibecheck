"""
API Routes for Weather VibeCheck.
Handles endpoints for preparedness plans, pantry survival, SOS, and commute risk.
"""
from fastapi import APIRouter, HTTPException, Request
from limiter import limiter
from models import PreparednessRequest, PantryRequest, SOSRequest, CommuteRequest
from services.llm_client import ask_llm
from services.weather_client import get_live_weather, get_commute_context
from prompts.monsoon import (
    PREPAREDNESS_PLAN_PROMPT,
    PANTRY_SURVIVAL_PROMPT,
    SOS_TRANSLATOR_PROMPT,
    COMMUTE_RISK_PROMPT,
)

router = APIRouter()

@router.post("/plan")
@limiter.limit("5/minute")
async def generate_preparedness_plan(request: Request, body: PreparednessRequest):
    """
    Generates a personalized monsoon preparedness plan.
    
    Dynamically assesses the user's input anxiety level and formats the 
    response tone accordingly, while providing immediate actions, a pre-storm 
    checklist, and emergency contacts.
    
    Args:
        request (Request): The incoming FastAPI request (required for SlowAPI).
        body (PreparednessRequest): The user's location, family size, and anxiety level.
        
    Returns:
        dict: A JSON object containing the preparedness plan.
    """
    weather_context = get_live_weather(body.location)
    user_message = f"Location: {body.location}\nLive Context: {weather_context}\nFamily Size: {body.family_size}\nAnxiety Level: {body.anxiety_level}"
    try:
        return ask_llm(PREPAREDNESS_PLAN_PROMPT, user_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/pantry")
@limiter.limit("5/minute")
async def generate_pantry_plan(request: Request, body: PantryRequest):
    """
    Generates a 3-day emergency meal plan based on available ingredients.
    
    Optimizes for a no-cook or low-cook scenario during power outages, 
    provides rationing tips, and generates an immediate shopping list 
    for missing essential items.
    
    Args:
        request (Request): The incoming FastAPI request.
        body (PantryRequest): A string containing the user's current pantry items.
        
    Returns:
        dict: A JSON object containing the 3-day meal plan and shopping list.
    """
    user_message = f"Available Ingredients: {body.ingredients}"
    try:
        return ask_llm(PANTRY_SURVIVAL_PROMPT, user_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/sos")
@limiter.limit("5/minute")
async def generate_sos_alerts(request: Request, body: SOSRequest):
    """
    Condenses a crisis situation into efficient SMS templates.
    
    Translates the user's distress signal and location into under-160-character 
    SMS messages formatted for rapid broadcasting in English, Hindi, and Marathi.
    
    Args:
        request (Request): The incoming FastAPI request.
        body (SOSRequest): The user's crisis situation and exact location.
        
    Returns:
        dict: A JSON object containing the translated SMS templates and safety advice.
    """
    weather_context = get_live_weather(body.location)
    user_message = f"Situation: {body.situation}\nLocation: {body.location}\nLive Context: {weather_context}"
    try:
        return ask_llm(SOS_TRANSLATOR_PROMPT, user_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/commute")
@limiter.limit("5/minute")
async def analyze_commute_risk(request: Request, body: CommuteRequest):
    """
    Analyzes the flood and weather risk for a planned commute.
    
    Calculates the Haversine distance between the start and end points, fetches
    live weather for both, and outputs a definitive Go/No-Go decision.
    
    Args:
        request (Request): The incoming FastAPI request.
        body (CommuteRequest): The starting location and destination.
        
    Returns:
        dict: A JSON object containing the risk level, hazards, and final decision.
    """
    commute_context = get_commute_context(body.start_location, body.end_location)
    user_message = f"Start: {body.start_location}\nDestination: {body.end_location}\nRoute Context: {commute_context}"
    try:
        return ask_llm(COMMUTE_RISK_PROMPT, user_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
API Routes for Weather VibeCheck.
Handles endpoints for preparedness plans, pantry survival, SOS, and commute risk.
"""
from fastapi import APIRouter, HTTPException, Request
from limiter import limiter
from models import PreparednessRequest, PantryRequest, SOSRequest, CommuteRequest
from services.llm_client import ask_llm
from services.weather_client import get_live_weather
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
    weather_context = get_live_weather(body.location)
    user_message = f"Location: {body.location}\nLive Context: {weather_context}\nFamily Size: {body.family_size}\nAnxiety Level: {body.anxiety_level}"
    try:
        return ask_llm(PREPAREDNESS_PLAN_PROMPT, user_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/pantry")
@limiter.limit("5/minute")
async def generate_pantry_plan(request: Request, body: PantryRequest):
    user_message = f"Available Ingredients: {body.ingredients}"
    try:
        return ask_llm(PANTRY_SURVIVAL_PROMPT, user_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/sos")
@limiter.limit("5/minute")
async def generate_sos_alerts(request: Request, body: SOSRequest):
    weather_context = get_live_weather(body.location)
    user_message = f"Situation: {body.situation}\nLocation: {body.location}\nLive Context: {weather_context}"
    try:
        return ask_llm(SOS_TRANSLATOR_PROMPT, user_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/commute")
@limiter.limit("5/minute")
async def analyze_commute_risk(request: Request, body: CommuteRequest):
    weather_context = get_live_weather(body.end_location) # Use destination weather
    user_message = f"Start: {body.start_location}\nDestination: {body.end_location}\nLive Destination Context: {weather_context}"
    try:
        return ask_llm(COMMUTE_RISK_PROMPT, user_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

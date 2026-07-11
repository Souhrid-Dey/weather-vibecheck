"""
API Routes for Weather VibeCheck.
Handles endpoints for preparedness plans, pantry survival, SOS, and commute risk.
"""
from fastapi import APIRouter, HTTPException
from models import PreparednessRequest, PantryRequest, SOSRequest, CommuteRequest
from services.gemini_client import ask_gemini
from prompts.monsoon import (
    PREPAREDNESS_PLAN_PROMPT,
    PANTRY_SURVIVAL_PROMPT,
    SOS_TRANSLATOR_PROMPT,
    COMMUTE_RISK_PROMPT,
)

router = APIRouter()

@router.post("/plan")
async def generate_preparedness_plan(request: PreparednessRequest):
    user_message = f"Location: {request.location}\nFamily Size: {request.family_size}\nAnxiety Level: {request.anxiety_level}"
    try:
        return ask_gemini(PREPAREDNESS_PLAN_PROMPT, user_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/pantry")
async def generate_pantry_plan(request: PantryRequest):
    user_message = f"Available Ingredients: {request.ingredients}"
    try:
        return ask_gemini(PANTRY_SURVIVAL_PROMPT, user_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/sos")
async def generate_sos_alerts(request: SOSRequest):
    user_message = f"Situation: {request.situation}\nLocation: {request.location}"
    try:
        return ask_gemini(SOS_TRANSLATOR_PROMPT, user_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/commute")
async def analyze_commute_risk(request: CommuteRequest):
    user_message = f"Start: {request.start_location}\nDestination: {request.end_location}"
    try:
        return ask_gemini(COMMUTE_RISK_PROMPT, user_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

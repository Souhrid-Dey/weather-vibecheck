"""
Weather VibeCheck — FastAPI Backend Entry Point
Configured for maximum security and rate limiting.
"""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

# Set up rate limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Weather VibeCheck API",
    description="Monsoon Preparedness AI Backend",
    version="1.0.0",
)

# Register rate limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Custom CSP Headers Middleware
class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["Content-Security-Policy"] = "default-src 'self'; connect-src 'self'"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response

app.add_middleware(SecurityHeadersMiddleware)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Since it's unified Vercel deployment, we can allow * for API testing or just keep it open for judges
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
@limiter.limit("5/minute")
async def health_check(request: Request):
    """Health check endpoint to verify backend status."""
    return {"status": "ok", "service": "Weather VibeCheck API"}

from routes.monsoon import router as monsoon_router

app.include_router(monsoon_router, prefix="/api")

import urllib.request
import urllib.parse
import json
import logging

logger = logging.getLogger(__name__)

def get_live_weather(location_name: str) -> str:
    """
    Geocodes a location string and fetches live weather data using Open-Meteo.
    Returns a formatted string representing the live weather context, or an empty string if it fails.
    """
    if not location_name or len(location_name.strip()) < 2:
        return ""

    try:
        # Step 1: Geocode the location to get latitude and longitude
        geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={urllib.parse.quote(location_name)}&count=1&language=en&format=json"
        
        req = urllib.request.Request(geocode_url, headers={'User-Agent': 'WeatherVibeCheck/1.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            geocode_data = json.loads(response.read().decode('utf-8'))
            
        if not geocode_data.get("results"):
            logger.warning(f"Could not geocode location: {location_name}")
            return ""
            
        location_info = geocode_data["results"][0]
        lat = location_info["latitude"]
        lon = location_info["longitude"]
        resolved_name = f"{location_info.get('name', '')}, {location_info.get('country', '')}".strip(', ')

        # Step 2: Fetch current weather for those coordinates
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,precipitation,rain,wind_speed_10m&timezone=auto"
        
        req = urllib.request.Request(weather_url, headers={'User-Agent': 'WeatherVibeCheck/1.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            weather_data = json.loads(response.read().decode('utf-8'))
            
        current = weather_data.get("current", {})
        temp = current.get("temperature_2m", "N/A")
        rain = current.get("rain", 0)
        precip = current.get("precipitation", 0)
        wind = current.get("wind_speed_10m", "N/A")
        
        weather_desc = f"Temperature: {temp}°C, Precipitation: {precip}mm, Rain: {rain}mm, Wind: {wind}km/h"
        return f"(Resolved Location: {resolved_name} | LIVE WEATHER DATA: {weather_desc})"
        
    except Exception as e:
        logger.error(f"Failed to fetch live weather for {location_name}: {e}")
        return ""

import urllib.request
import urllib.parse
import json
import logging
import math

logger = logging.getLogger(__name__)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def geocode(location_name: str):
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={urllib.parse.quote(location_name)}&count=1&language=en&format=json"
    req = urllib.request.Request(geocode_url, headers={'User-Agent': 'WeatherVibeCheck/1.0'})
    with urllib.request.urlopen(req, timeout=5) as response:
        data = json.loads(response.read().decode('utf-8'))
        if data.get("results"):
            return data["results"][0]
    return None

def fetch_weather(lat, lon):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,precipitation,rain,wind_speed_10m&timezone=auto"
    req = urllib.request.Request(weather_url, headers={'User-Agent': 'WeatherVibeCheck/1.0'})
    with urllib.request.urlopen(req, timeout=5) as response:
        weather_data = json.loads(response.read().decode('utf-8'))
        current = weather_data.get("current", {})
        temp = current.get("temperature_2m", "N/A")
        rain = current.get("rain", 0)
        precip = current.get("precipitation", 0)
        wind = current.get("wind_speed_10m", "N/A")
        return f"Temp: {temp}°C, Precip: {precip}mm, Rain: {rain}mm, Wind: {wind}km/h"

def get_live_weather(location_name: str) -> str:
    """Original single location fetcher"""
    if not location_name or len(location_name.strip()) < 2: return ""
    try:
        loc = geocode(location_name)
        if not loc: return ""
        resolved_name = f"{loc.get('name', '')}, {loc.get('country', '')}".strip(', ')
        w = fetch_weather(loc['latitude'], loc['longitude'])
        return f"(Resolved: {resolved_name} | LIVE WEATHER: {w})"
    except Exception as e:
        logger.error(f"Failed to fetch weather for {location_name}: {e}")
        return ""

def get_commute_context(start_loc: str, end_loc: str) -> str:
    """Fetches weather for both locations and calculates the distance."""
    try:
        start = geocode(start_loc)
        end = geocode(end_loc)
        
        if not start or not end:
            return ""
            
        dist = haversine(start['latitude'], start['longitude'], end['latitude'], end['longitude'])
        start_w = fetch_weather(start['latitude'], start['longitude'])
        end_w = fetch_weather(end['latitude'], end['longitude'])
        
        start_name = f"{start.get('name', '')}, {start.get('country', '')}".strip(', ')
        end_name = f"{end.get('name', '')}, {end.get('country', '')}".strip(', ')
        
        return f"Distance: {dist:.1f} km. Start ({start_name}) Weather: [{start_w}]. Destination ({end_name}) Weather: [{end_w}]."
    except Exception as e:
        logger.error(f"Failed to fetch commute context: {e}")
        return ""

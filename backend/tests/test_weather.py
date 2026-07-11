from services.weather_client import haversine
import math

def test_haversine_same_point():
    """Distance between the same point should be 0."""
    dist = haversine(19.0760, 72.8777, 19.0760, 72.8777)
    assert dist == 0.0

def test_haversine_known_distance():
    """Distance between Mumbai and Pune is ~118km."""
    # Mumbai
    lat1, lon1 = 19.0760, 72.8777
    # Pune
    lat2, lon2 = 18.5204, 73.8567
    
    dist = haversine(lat1, lon1, lat2, lon2)
    assert math.isclose(dist, 118, abs_tol=5.0) # allow 5km variance

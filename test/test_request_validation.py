from app.geo_resolver.geo_fetcher.geo_fetcher import GeoFetcher
from app.geo_resolver.geo_resolver import GeoResolver
from app.models.location_request import LocationRequest
from app.models.location_response import LocationResponse

def test_valid_ip():
    ip = "192.168.1.1"
    request = LocationRequest(reqId="123", ip=ip)
    assert request.ip == ip


def test_invalid_ip():
    invalid_ip = "256.300.400.500"
    try:
        LocationRequest(reqId="123", ip=invalid_ip)
    except ValueError as e:
        assert "Invalid IP address format" in str(e)

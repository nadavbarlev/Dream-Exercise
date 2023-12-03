import pytest
from app.geo_resolver.geo_fetcher.geo_fetcher import GeoFetcher
from app.geo_resolver.geo_resolver import GeoResolver
from app.models.location_request import LocationRequest
from app.models.location_response import LocationResponse

pytest_plugins = ('pytest_asyncio',)

class MockGeoFetcher(GeoFetcher):
    def __init__(self, prepared_response: LocationResponse):
        self.response = prepared_response

    async def fetch_geolocation(self, request):
        return self.response

@pytest.mark.asyncio
async def test_geo_resolver():
    request_id = "1234"
    resolver = GeoResolver()
    geo_fetcher = MockGeoFetcher(
        prepared_response=LocationResponse(
            reqId=request_id, countryCode="US", lat=37.7749, lon=-122.4194
        )
    )
    request = LocationRequest(reqId=request_id, ip="192.168.1.1")
    response = await resolver.resolve(geo_fetcher, request)
    assert response.countryCode == "US"
    assert response.lat == 37.7749
    assert response.lon == -122.4194

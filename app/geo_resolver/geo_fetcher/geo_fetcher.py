import aiohttp
from abc import ABC
from app.models.location_request import LocationRequest
from app.models.location_response import LocationResponse


class GeoFetcher(ABC):
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def fetch_geolocation(self, request: LocationRequest) -> LocationResponse:
        pass

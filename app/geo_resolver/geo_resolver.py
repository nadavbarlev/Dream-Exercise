from cachetools import TTLCache
from app.models.location_request import LocationRequest
from app.models.location_response import LocationResponse
from app.geo_resolver.geo_fetcher.geo_fetcher import GeoFetcher


class GeoResolver:
    _cache_ttl: int = 86400
    _cache_max_size: int = 100

    def __init__(self):
        self._cache = TTLCache(maxsize=self._cache_max_size, ttl=self._cache_ttl)

    async def resolve(
        self, geo_fetcher: GeoFetcher, request: LocationRequest
    ) -> LocationResponse:
        if request.ip in self._cache:
            return self._cache[request.ip]



        geolocation_response = await geo_fetcher.fetch_geolocation(request)
        self._cache[request.ip] = geolocation_response
        return geolocation_response

import aiohttp
from app.geo_resolver.geo_fetcher.geo_fetcher import GeoFetcher
from app.models.location_request import LocationRequest
from app.models.location_response import LocationResponse


class IpApiGeoFethcer(GeoFetcher):
    async def fetch_geolocation(self, request: LocationRequest) -> LocationResponse:
        try:
            async with self.session.get(
                f"http://ip-api.com/json/{request.ip}"
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    return LocationResponse(
                        reqId=request.reqId,
                        countryCode=data["countryCode"],
                        lat=data["lat"],
                        lon=data["lon"],
                    )
                else:
                    return {"error": "Failed to fetch location data"}
        except aiohttp.ClientError as e:
            return {"error": str(e)}

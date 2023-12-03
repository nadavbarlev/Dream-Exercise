import aiohttp
from app.geo_resolver.geo_fetcher.geo_fetcher import GeoFetcher
from app.models.location_request import LocationRequest
from app.models.location_response import LocationResponse


class IpInfoGeoFetcher(GeoFetcher):
    async def fetch_geolocation(self, request: LocationRequest) -> LocationResponse:
        try:
            # TODO: Implement a more secure way to store and handle the access token
            access_token = "b68896fb1f154e"
            async with self.session.get(
                f"http://ipinfo.io/{request.ip}?token={access_token}"
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    return LocationResponse(
                        reqId=request.reqId,
                        countryCode=data["country"],
                        lat=data["loc"].split(",")[0],
                        lon=data["loc"].split(",")[1]
                    )
                else:
                    return { "error": "Failed to fetch location data" }
        except aiohttp.ClientError as e:
            return { "error": str(e) }



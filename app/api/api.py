import os
from app.models.location_request import LocationRequest
from app.models.location_response import LocationResponse
from app.geo_resolver.geo_resolver import GeoResolver, GeoFetcher
from app.geo_resolver.geo_fetcher.ip_api_geo_fetcher import IpApiGeoFethcer
from app.geo_resolver.geo_fetcher.ip_info_geo_fetcher import IpInfoGeoFetcher

GEO_FETCHER: GeoFetcher = None
geo_fetcher_name = os.environ.get("GEO_FETCHER", "ip-api")


async def get_location(request: LocationRequest) -> LocationResponse:
    global GEO_FETCHER
    if not GEO_FETCHER and geo_fetcher_name == "ip-api":
        GEO_FETCHER = IpApiGeoFethcer()
    else:
        GEO_FETCHER = IpInfoGeoFetcher()
    return await GeoResolver().resolve(GEO_FETCHER, request)

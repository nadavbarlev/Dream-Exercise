from pydantic import BaseModel


class LocationResponse(BaseModel):
    reqId: str
    countryCode: str
    lat: float
    lon: float

from .api import api
import uvicorn
from fastapi import FastAPI
from app.models.location_request import LocationRequest
from app.models.location_response import LocationResponse

global app
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Dream Exercise - Loction Service"}


@app.post("/location")
async def get_location(request: LocationRequest) -> LocationResponse:
    return await api.get_location(request)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8123)

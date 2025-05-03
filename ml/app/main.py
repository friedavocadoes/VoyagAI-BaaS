from fastapi import FastAPI
from pydantic import BaseModel
from .recommend import recommend_trip

app = FastAPI()

class TripRequest(BaseModel):
    sentiment: str
    location: str
    budget: int

@app.post("/recommend")
def get_trip_plan(request: TripRequest):
    result = recommend_trip(request.sentiment, request.location, request.budget)
    return result

from pydantic import BaseModel
from .recommend import recommend_trip
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
import os
from .json_parser import json_parser

# app = FastAPI()

# class TripRequest(BaseModel):
#     sentiment: str
#     location: str
#     budget: int

# @app.post("/recommend")
# def get_trip_plan(request: TripRequest):
#     result = recommend_trip(request.sentiment, request.location, request.budget)
#     return result




app = FastAPI()

# Set this from an environment variable or directly (not recommended)
# print("this is", os.getenv("GEM_API_KEY"))
client = genai.Client(api_key=os.getenv("GEM_API_KEY"))


class TravelRequest(BaseModel):
    sentiment: str
    location: str
    budget: int

@app.post("/generate-destinations")
async def generate_destinations(data: TravelRequest):
    prompt = f"""
    You are a travel recommendation expert.

    A user from "{data.location}" has a budget of ₹{data.budget}". 
    They are looking for a travel destination that matches this mood or statement: "{data.sentiment}"

    Based on the location and budget, suggest 3 to 5 suitable tourist destinations the user can actually travel to, 
    either locally or nearby states. These must be:

    1. Realistic to travel to under the given budget (include travel + basic stay)
    2. Align with the mood or vibe of the user
    3. Popular or worth visiting

    Respond in this exact JSON format (do not add json formatting text):

    [
      {{
        "place": "Place Name",
        "reason": "Why this place suits the mood and budget",
        "estimated_cost": "Total cost estimation"
      }},
      ...
    ]
    """

    try:
        # response = client.models.generate_content(model="gemini-2.0-flash", contents="Explain how AI works in a few words")
        model = "gemini-2.0-flash"
        # response = model.generate_content(prompt)
        response = client.models.generate_content(model=model, contents=prompt)
        parsed_json = json_parser(response.text)
        if parsed_json:
            return {"results": parsed_json}
        else:
            raise HTTPException(status_code=500, detail="Failed to parse Gemini response as JSON")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

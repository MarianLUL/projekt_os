import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, Response, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv


load_dotenv()

app = FastAPI(title="Weather Demo API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

VISUALCROSSING_API_KEY = os.getenv("VISUALCROSSING_API_KEY")
VC_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"


@app.get("/")
def root():
    """Serve frontend index.html so the UI is available at the same origin as the API."""
    # try to serve frontend/index.html located next to project
    here = os.path.dirname(__file__)
    index_path = os.path.abspath(os.path.join(here, '..', 'index.html'))
    if os.path.exists(index_path):
        return FileResponse(index_path, media_type='text/html')
    return {"message": "Weather Demo API"}


@app.get("/weather/{city}")
def get_weather(city: str):
    if not VISUALCROSSING_API_KEY:
        raise HTTPException(status_code=500, detail="VISUALCROSSING_API_KEY not set")

    # Visual Crossing timeline API accepts a location string (city) directly
    url = f"{VC_URL}/{requests.utils.requote_uri(city)}"
    params = {
        "key": VISUALCROSSING_API_KEY,
        "unitGroup": "metric",
        "include": "current",
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=str(e))

    if resp.status_code != 200:
        # avoid returning raw HTML from external services; provide concise error
        text = resp.text
        safe_msg = text
        if text.strip().startswith('<'):
            safe_msg = f"External API returned status {resp.status_code}"
        raise HTTPException(status_code=resp.status_code, detail=safe_msg)

    data = resp.json()
    # Visual Crossing returns currentConditions
    current = data.get("currentConditions", {})
    result = {
        "city": data.get("resolvedAddress") or city,
        "country": None,
        "temperature": current.get("temp"),
        "feels_like": current.get("feelslike") or current.get("feelslike_c"),
        "humidity": current.get("humidity"),
        "pressure": current.get("pressure"),
        "description": current.get("conditions"),
        "wind_speed": current.get("windspeed"),
    }
    return result

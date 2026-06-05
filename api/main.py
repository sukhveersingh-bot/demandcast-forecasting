"""Forecast API."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Forecast API")


class ForecastRequest(BaseModel):
    store_id: int
    item_id: int
    horizon_days: int = 30


@app.post("/forecast")
def forecast(req: ForecastRequest) -> dict:
    return {
        "model": "tft",
        "forecast": [],
        "store_id": req.store_id,
        "item_id": req.item_id,
    }

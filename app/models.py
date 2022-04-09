from pydantic import BaseModel

class Weather(BaseModel):
    name: str
    country: str
    max: float
    min: float
    avg: float
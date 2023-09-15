from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from english_sentiment import review_rating

app = FastAPI()

@app.get("/")
async def home():
    return str("First view")

#----------------------------
class RateRequest(BaseModel):
    input: str
class RateResponse(BaseModel):
    Positive: float
    Neutral: float
    Negative: float


@app.post("/string_to_rate/", response_model=RateResponse)
async def rate_a_string(request_data: RateRequest):
    try:
        rating = await review_rating(request_data.input)
        return RateResponse(Positive=rating[2], Neutral=rating[1], Negative=rating[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

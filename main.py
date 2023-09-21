from fastapi import FastAPI, HTTPException
from english_sentiment import review_rating
from request_and_response import Request, Response

app = FastAPI()

@app.get("/")
async def home():
    return "English sentiment."

@app.post("/eng_sentiment/", response_model=Response)
async def rate_a_string(request_data: Request):
    try:
        rating = await review_rating(request_data.input)
        return Response(output=rating)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

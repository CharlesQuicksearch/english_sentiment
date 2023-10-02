import json

import schedule
import uvicorn

from Config_Logger import logger
from Config_Logger.logger import logging
from english_sentiment import rate
from fastapi import FastAPI, HTTPException
from request_and_response import Request, Response

app = FastAPI()

logger.config_logger()

#Start writing logs in a new logging file
schedule.every().day.at("00:00").do(logger.config_logger)

with open("config.json", "r") as f:
    config = json.load(f)

host = config.get("host")
port = config.get("port")


@app.get("/")
async def home():
    return "English sentiment."


@app.post("/eng_sentiment/", response_model=Response)
async def rate_a_string(request_data: Request):
    try:
        logging.info(f"Request: {request_data.input}")
        rating = await rate(request_data.input)
        logging.info(f"200 {rating}")
        return Response(output=rating)
    except Exception as e:
        logging.info(f"500 {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host=host, port=int(port))

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import asyncio
import uuid

app = FastAPI()

"""
Takes in
{
    "betId"     : "some_uuid"
    ,"currency" : "USD"
    ,"wonAmount": "1000"
    ,"email"    : "john.doe@gmail.com"
}
"""
# @app.post("/internal_market/bet")
# async def placeBet(request: Request):
#     return await request.json()
@app.post("/internal_notification/email")
def placeBet(request: Request):
    body = asyncio.run(request.json())

    bets_cache[body["betId"]] = body


    ##TODO add emailing function???

    return JSONResponse(status_code=200, content="Notified")

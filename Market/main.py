#:8081
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import asyncio
import uuid

app = FastAPI()

bets_cache = {
}

"""
Takes in
{
    "betId"     : "some_uuid"
    ,"matchDate": "2022-12-18"
    ,"team"     : "Argentina"
    ,"result"   : "win"
    ,"currency" : "USD"
    ,"amount"   : "100"
    ,"email"    : "john.doe@gmail.com"
}
"""
# @app.post("/internal_market/bet")
# async def placeBet(request: Request):
#     return await request.json()
@app.post("/internal_market/bet")
def placeBet(request: Request):
    body = asyncio.run(request.json())

    bets_cache[body["betId"]] = body

    # return JSONResponse(status_code=404, content={"details": f"testing"})

    return {
        "betId": body["betId"]
    }


@app.get("/internal_market/bet")
def getBet():
    # return JSONResponse(status_code=404, content={"details": f"testing"})
    return bets_cache


@app.get("/internal_market/bet/{betId}")
def getBet(betId):
    if betId in bets_cache:
        return bets_cache[betId]
    else:
        return JSONResponse(status_code=404, content={"details": f"No bet was found with this betId: '{betId}'"})
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests
import asyncio
import uuid

app = FastAPI()

internal_notification_url= f"http://localhost:8082/internal_notification/email"


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

    body["status"] = "PENDING"
    bets_cache[body["betId"]] = body

    return {
        "betId": body["betId"]
    }


@app.get("/internal_market/bet")
def getBet():
    return bets_cache


@app.get("/internal_market/bet/{betId}")
def getBet(betId):
    if betId in bets_cache:
        return bets_cache[betId]
    else:
        return JSONResponse(status_code=404, content={"details": f"No bet was found with this betId: '{betId}'"})


@app.get("/internal_market/bet/notify/")
def decideBets():

    for bet in bets_cache:
        post_param = {}
        post_param["betId"]     = bets_cache[bet]["betId"]
        post_param["currency"]  = bets_cache[bet]["currency"]
        post_param["wonAmount"] = int(bets_cache[bet]["amount"]) * 10
        post_param["email"]     = bets_cache[bet]["email"]

        if (
            bets_cache[bet]["status"] == "WON"
        ):
            post_response = requests.post(internal_notification_url, json=post_param)

            if post_response.status_code == 200:
                bets_cache[bet]["status"] = "DONE"
                continue
            else:
                continue

    return JSONResponse(status_code=200, content="Notified winners")


@app.get("/internal_market/bet/hack_set_all_win/")
def decideBets():
    for bet in bets_cache:
        bets_cache[bet]["status"] = "WON"

    return JSONResponse(status_code=200, content="hack completed ;)")

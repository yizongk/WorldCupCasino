from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests
import asyncio
import uuid
import json

app = FastAPI()

internal_market_url= f"http://localhost:8082/internal_market/bet"


"""
Takes in
{
    "matchDate" : "2022-12-18"
    ,"team"     : "Argentina"
    ,"result"   : "win"
    ,"currency" : "USD"
    ,"amount"   : "100"
    ,"email"    : "john.doe@gmail.com"
}
"""
# @app.post("/market/bet")
# async def placeBet(request: Request):
#     print("Calling internal market api with:\n{}".format(await request.json()))
#     return await request.json()
@app.post("/market/bet")
def placeBet(request: Request):
    body = asyncio.run(request.json())

    new_bet_id = uuid.uuid4()
    body["betId"] = f"{new_bet_id}"

    post_response = requests.post(internal_market_url, json=body)

    if post_response.status_code == 200:
        return {
            "betId": post_response.json()["betId"]
        }
    else:
        return JSONResponse(
            status_code=post_response.status_code
            ,content=post_response.json()
        )


@app.get("/market/bet")
def getBet():
    get_response = requests.get(internal_market_url)

    if get_response.status_code == 200:
        return get_response.json()
    else:
        return JSONResponse(
            status_code=get_response.status_code
            ,content=get_response.json()
        )


@app.get("/market/bet/{betId}")
def getBet(betId):
    get_response = requests.get(f"{internal_market_url}/{betId}")

    if get_response.status_code == 200:
        return get_response.json()
    else:
        return JSONResponse(
            status_code=get_response.status_code
            ,content=get_response.json()
        )
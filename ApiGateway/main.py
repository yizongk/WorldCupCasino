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
    "matchDate": "2022-12-18"
    ,"team": "Argentina"
    ,"result": "win"
    ,"currency": "USD"
    ,"amount": "100"
    ,"email": "john.doe@gmail.com"
}
"""
# @app.post("/market/bet")
# async def placeBet(request: Request):
#     print("Calling internal market api with:\n{}".format(await request.json()))
#     return await request.json()
@app.post("/market/bet")
def placeBet(request: Request):
    body = asyncio.run(request.json())
    print("Calling internal market api with:\n{}".format(body))

    new_bet_id = uuid.uuid4()
    print(type(new_bet_id))
    bets_cache[f"{new_bet_id}"] = body

    return {
        "betId": new_bet_id
    }


@app.get("/market/bet")
def getBet():
    print('all bet query')
    return bets_cache


@app.get("/market/bet/{betId}")
def getBet(betId):
    if betId in bets_cache:
        print('foundc')
        return bets_cache[betId]
    else:
        print('not found')
        return JSONResponse(status_code=404, content={"details": f"No bet was found with this betId: '{betId}'"})
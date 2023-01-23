from fastapi import FastAPI, Request
import asyncio

app = FastAPI()

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
    return body

@app.get("/market/bet")
async def getBet(betId):
    return {
        "message": "Hello World!"
        ,"betId": betId
        ,"": ""
        ,"": ""
        ,"": ""
    }

@app.get("/market/bet/{betId}")
async def getBet(betId):
    return {
        "message": "Hello World!"
        ,"betId": betId
        ,"": ""
        ,"": ""
        ,"": ""
    }
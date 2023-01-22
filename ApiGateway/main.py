from fastapi import FastAPI

app = FastAPI()

@app.post("/market/bet")
async def placeBet():
    return {
        "team": "Hello World!"
        ,"": ""
        ,"": ""
        ,"": ""
        ,"": ""
    }

@app.get("/market/bet")
async def getBet():
    return return {
        "message": "Hello World!"
        ,"": ""
        ,"": ""
        ,"": ""
        ,"": ""
    }
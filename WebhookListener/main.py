from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import asyncio
import uuid

app = FastAPI()

notification_received = 0

@app.post("/listen")
def listen(request: Request):
    if (asyncio.run(request.body()) is not None     # If body is not empty
        and asyncio.run(request.body()) != b''      # If body is not empty byte
    ):
        body = asyncio.run(request.json())

    global notification_received
    notification_received += 1

    return JSONResponse(status_code=200, content="Recevied")

@app.get("/client_notified")
def getStats(request: Request):
    return JSONResponse(status_code=200, content=f"Received {notification_received} notifications")

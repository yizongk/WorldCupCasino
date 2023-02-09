from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests
import asyncio
import uuid

app = FastAPI()

client_web_hook_url = f"http://localhost:8084/listen"

"""
Takes in
{
    "betId"     : "some_uuid"
    ,"currency" : "USD"
    ,"wonAmount": "1000"
    ,"email"    : "john.doe@gmail.com"
}
"""
@app.post("/internal_notification/email")
def notifyClient(request: Request):
    body = asyncio.run(request.json())

    post_response = requests.post(client_web_hook_url, json=body)

    return JSONResponse(status_code=200, content="Notified")

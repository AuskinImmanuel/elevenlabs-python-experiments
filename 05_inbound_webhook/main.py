"""Inbound webhook: Twilio number -> FastAPI -> ElevenAgent.

Status: stub.

Plan:
  - FastAPI endpoint /voice that Twilio hits on inbound call
  - Returns TwiML that connects the call to the ElevenLabs SIP/WebRTC endpoint
  - Run locally with ngrok or fly.io; point the Twilio number's webhook at it
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health() -> dict:
    return {"status": "ok"}


@app.post("/voice")
def voice() -> dict:
    raise NotImplementedError("Pending: TwiML response that hands the call to ElevenAgent")

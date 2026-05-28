# 05 — inbound webhook

A FastAPI service that sits between a Twilio phone number and an ElevenAgent. Caller dials the Twilio number → Twilio hits this webhook → response hands the call off to the agent.

## Run

```bash
uvicorn 05_inbound_webhook.main:app --reload --port 8000
```

Expose with ngrok or similar, then set the Twilio number's voice webhook to `https://<tunnel>/voice`.

## What I'm trying to learn

- How TwiML actually hands a call to an external SIP/WebRTC endpoint
- Where the latency is in this chain
- What breaks when the agent transfers mid-call

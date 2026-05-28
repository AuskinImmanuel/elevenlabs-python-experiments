"""Tool webhook: agent captures contact info -> write a HubSpot contact.

Status: stub.

Plan:
  - FastAPI endpoint that the ElevenAgent calls as a tool
  - Receives name, email, intent from the agent
  - Creates / updates a HubSpot contact with hubspot-api-client
  - Returns a confirmation string the agent can speak back
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ContactPayload(BaseModel):
    name: str
    email: str
    intent: str


@app.post("/hubspot/contact")
def write_contact(payload: ContactPayload) -> dict:
    raise NotImplementedError("Pending: hubspot-api-client contact create/update")

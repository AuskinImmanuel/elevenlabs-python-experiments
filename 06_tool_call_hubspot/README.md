# 06 — tool call writes to HubSpot

The agent collects a name, email, and intent during the call, then calls this webhook as a tool. The webhook writes the contact to a HubSpot free developer sandbox.

## Run

```bash
uvicorn 06_tool_call_hubspot.main:app --reload --port 8001
```

Configure the tool inside the ElevenAgent: name `write_hubspot_contact`, URL pointing at this webhook, body matches `ContactPayload`.

## What I'm trying to learn

- How the agent waits for (or doesn't wait for) the tool response
- What the response shape should look like for the agent to speak it back naturally
- HubSpot dedupe behavior on repeat captures of the same email

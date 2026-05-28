# elevenlabs-python-experiments

A working sandbox for the parts of voice-agent work I don't usually touch myself: Python scripting against the ElevenLabs SDK, Twilio telephony, and basic third-party integrations.

I'm Auskin Immanuel. Day job is voice-agent design — prompts, scopes, evals — and at that layer I'm fluent. The Python that wires it all together is usually written by engineering. This repo is me closing that gap, by hand, one small script at a time.

## Why this exists

Forward-deployed voice work doesn't stop at the prompt. It runs through Python scripts that talk to the platform API, FastAPI services that bridge to a phone number, tool-call webhooks that write to a CRM, eval scripts that pull a transcript and score it. None of that is hard. It's just hours-in-the-editor I haven't put in yet. So I'm putting them in.

Sandbox quality, not production quality. The point is to *do* the integration, learn the gotchas, and have a runnable thing to point at.

## What's here

Each numbered file is one self-contained experiment. Run them in order or in any order; they don't share state.

| # | File | What it does |
|---|---|---|
| 01 | [01_list_voices.py](01_list_voices.py) | List voices in the workspace via the ElevenLabs Python SDK. The smoke test that proves env + key + SDK path all work. |
| 02 | [02_create_agent.py](02_create_agent.py) | Create an ElevenAgent programmatically from a system prompt file. |
| 03 | [03_update_agent_prompt.py](03_update_agent_prompt.py) | Update an existing agent's prompt without recreating it. |
| 04 | [04_outbound_call.py](04_outbound_call.py) | Place an outbound call via the Twilio bridge to a given number. |
| 05 | [05_inbound_webhook/](05_inbound_webhook/) | FastAPI service. Twilio number → webhook → ElevenAgent. |
| 06 | [06_tool_call_hubspot/](06_tool_call_hubspot/) | Agent captures contact info during a call → tool webhook → HubSpot contact written. |
| 07 | [07_transcript_eval.py](07_transcript_eval.py) | Fetch a finished call's transcript and score it against a rubric. |
| 08 | [08_multi_llm_compare.py](08_multi_llm_compare.py) | Same prompt, different LLM backends. Log latency + output side-by-side. |

[scenarios/](scenarios/) holds the agent prompts I'm experimenting against — financial-services flows (card dispute, balance check). The prompt thinking behind them lives in my [voice-agent-prompting](https://github.com/AuskinImmanuel/voice-agent-prompting) repo.

[notes/learnings.md](notes/learnings.md) is the running log: what surprised me, what broke, what I want to ask the team about.

## Running anything here

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in your keys
python 01_list_voices.py
```

You need: an ElevenLabs API key, a Twilio account (trial is fine) with a number, and a HubSpot free developer account for `06_*`.

## What this isn't

- Not production code. No retry logic, no test suite, no observability.
- Not a polished demo. There's no Loom, no architecture diagram.
- Not healthcare. I have plenty of healthcare depth at work; this repo is for the surface I'm new to.

## Reach me

[LinkedIn](https://www.linkedin.com/in/auskin-immanuel/)

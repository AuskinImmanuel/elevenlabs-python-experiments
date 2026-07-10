# elevenlabs-python-experiments

A working sandbox: Python scripts against the ElevenLabs SDK, one small experiment per file.

I'm Auskin Immanuel. Day job is voice-agent design. My production output is prompts, specs, and evals; this repo is the scripting layer that sits under and around that work. Create an agent from a prompt file, patch its prompt, pull a transcript and score it. The calls my specs describe, run by my own hand.

## Why this exists

A spec that says "patch the agent's prompt, keep the rest of the config" is stronger when I've run that exact call and watched what came back. Same for evals: before I trust a scoring pipeline, I want to have pulled a raw transcript and seen its actual shape. Each script here is one of those calls, done end to end, with the gotchas written down as I hit them.

Sandbox quality on purpose. No shared helpers, no abstractions, every file readable top to bottom in one sitting.

## What's here

Each numbered file is one self-contained experiment. They don't share state.

| # | File | Status | What it does |
|---|---|---|---|
| 01 | [01_list_voices.py](01_list_voices.py) | working | List voices in the workspace. The smoke test that proves env + key + SDK path all work. |
| 02 | [02_create_agent.py](02_create_agent.py) | working | Create an agent from a system prompt file, print the new agent id. |
| 03 | [03_update_agent_prompt.py](03_update_agent_prompt.py) | working | Patch an existing agent's prompt without recreating it or touching the rest of its config. |
| 04 | [04_outbound_call.py](04_outbound_call.py) | planned | Place an outbound call via the Twilio bridge to a given number. |
| 05 | [05_transcript_eval.py](05_transcript_eval.py) | working | Fetch a finished call's transcript and score it against a deterministic rubric. Pure Python, no LLM judge. |
| 06 | [06_multi_llm_compare.py](06_multi_llm_compare.py) | planned | Same prompt, different LLM backends. Log latency and output side by side. |

[scenarios/](scenarios/) holds the agent prompts I'm experimenting against: financial-services flows (card dispute, balance check). The prompt thinking behind them lives in my [voice-agent-prompting](https://github.com/AuskinImmanuel/voice-agent-prompting) repo.

[notes/learnings.md](notes/learnings.md) is the running log: what surprised me, what broke, what I want to ask the team about.

## Running anything here

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in your keys
python 01_list_voices.py
```

You need an ElevenLabs API key. Twilio only matters once 04 lands, and the LLM provider keys only matter for 06.

## What this isn't

- Not production code. No retry logic, no test suite, no observability.
- Not a polished demo. There's no Loom, no architecture diagram.
- Not healthcare. I have plenty of healthcare depth at work; here I run financial-services scenarios so the two never mix.

## Reach me

[LinkedIn](https://www.linkedin.com/in/auskin-immanuel/)

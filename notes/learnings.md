# Learnings

Running log. Surprises, gotchas, things to ask the ElevenLabs team about.

Format: date, what I was doing, what happened, what I changed.

---

## 2026-05-28: repo bootstrap

Stubbed out the eight experiment scripts and the two FastAPI services. Working through them in order. `01_list_voices.py` runs end-to-end, which confirms the SDK install and the API key path are fine.

Open question for the platform team when I have a real one to ask: how the tool-call response shape affects the speech-back latency. I see it at work, never timed it.

## 2026-07-10: 02_create_agent.py, first agent created from code

My stub plan said `client.agents.create(...)`. Wrong twice. The agents surface lives at `client.conversational_ai.agents`, and the prompt is not a top-level field. It nests three levels down: `conversation_config.agent.prompt.prompt`. The surprise: the `prompt` field on `AgentConfig` is typed with the response model, `PromptAgentApiModelOutput`, even on create. I imported the matching `...Input` model first, like the naming suggests, and pydantic rejected it with a validation error. The generated client reuses the output type on the write path here; the input class exists in the package but nothing accepts it.

## 2026-07-10: 03_update_agent_prompt.py, patching a prompt without touching the rest

The update call takes the same `conversation_config` shape as create, so I worried a prompt-only config would wipe the voice and LLM settings on the agent. It doesn't. The surprise: the SDK drops unset fields from the request body entirely. I ran the body through the SDK's own encoder before trusting it, and a config built with only the prompt text set comes out as `{"agent": {"prompt": {"prompt": "..."}}}`. The PATCH endpoint merges that in and leaves the rest alone. Also, update returns the full agent object rather than a slim acknowledgment, which makes the confirmation print easy.

## 2026-07-10: 05_transcript_eval.py, deterministic transcript scoring

`client.conversational_ai.conversations.get(conversation_id)` returns the whole conversation, with `transcript` as a list of turns and `role` either `user` or `agent`. The surprise: `message` is optional, and it really is None on turns where the agent only fires a tool call. My first pass joined agent messages naively and crashed on exactly that, so every text check now filters None first. The rubric itself stayed pure Python: required slots by substring, forbidden phrases by substring, digit read-back by a regex for runs of four or more digits. Known blind spot: a year like 2026 in an agent turn trips the digit check.

## 2026-07-10: cut the Twilio webhook and HubSpot services

Deleted the two FastAPI service directories (inbound webhook, HubSpot tool call). Both stalled on account plumbing: tunnel setup, webhook registration, sandbox CRM credentials. Scripts against the platform API teach me more per hour than account plumbing, so the repo now sticks to those. Outbound calling (04) and the multi-LLM compare (06) stay on the planned list.

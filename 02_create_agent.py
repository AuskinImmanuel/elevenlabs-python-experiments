"""Create an ElevenAgent programmatically from a prompt file.

Status: stub. Wire up against ElevenLabs Agents API.

Plan:
  - Read a system prompt from scenarios/card_dispute.md
  - POST to the agents endpoint with name, prompt, voice_id, llm config
  - Print the returned agent_id
  - Verify in the ElevenLabs dashboard
"""


def main() -> None:
    raise NotImplementedError("Pending: ElevenLabs agents API call")


if __name__ == "__main__":
    main()

"""Place an outbound call via the ElevenLabs + Twilio bridge.

Status: stub.

Plan:
  - Take an agent_id and a destination phone number
  - Call the outbound endpoint (ElevenLabs initiates, Twilio carries)
  - Print the conversation_id so 05_transcript_eval.py can pick it up later
"""


def main() -> None:
    raise NotImplementedError("Pending: outbound call trigger")


if __name__ == "__main__":
    main()

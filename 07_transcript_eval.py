"""Fetch a finished call's transcript and score it against a rubric.

Status: stub.

Plan:
  - Take a conversation_id
  - Fetch the transcript via the ElevenLabs API
  - Run it against a small rubric (intent captured? required slots filled? tone appropriate?)
  - Print scored result + per-criterion notes
"""


def main() -> None:
    raise NotImplementedError("Pending: transcript fetch + rubric scoring")


if __name__ == "__main__":
    main()

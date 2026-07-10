"""Fetch a finished call's transcript and score it against a rubric.

Usage:
    python 05_transcript_eval.py <conversation_id>

No LLM judge. Every check is plain string matching over the transcript,
so the same transcript always gets the same score.

To get a conversation to score: run 02_create_agent.py, open the new
agent in the ElevenLabs dashboard, and place a test call from there.
The conversation shows up in the call history shortly after the call
ends; copy its id and pass it to this script.

Rubric (written against scenarios/card_dispute.md):
  1. Required slots. The agent asked for the last 4 of the card, asked
     for date of birth or mobile, and confirmed a dispute reason from
     the fixed set.
  2. Forbidden phrases. The agent never editorialised about the
     merchant or speculated about fraud.
  3. Digit read-back. Identifiers get read digit by digit, so any run
     of four or more digits in an agent turn fails the check.
"""

import os
import re
import sys

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

REQUIRED_SLOTS = {
    "asked for last 4 of card": ("last 4", "last four"),
    "asked for DOB or mobile": ("date of birth", "mobile"),
    "confirmed a dispute reason": (
        "not authorised",
        "not authorized",
        "wrong amount",
        "duplicate",
        "not received",
        "not as described",
    ),
}

FORBIDDEN_PHRASES = (
    "scam",
    "sounds like fraud",
    "definitely fraud",
    "fraudulent merchant",
    "i guarantee",
)

DIGIT_RUN = re.compile(r"\d{4,}")


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: python 05_transcript_eval.py <conversation_id>")
        sys.exit(1)

    load_dotenv()
    client = ElevenLabs(api_key=os.environ["ELEVENLABS_API_KEY"])

    conversation = client.conversational_ai.conversations.get(sys.argv[1])

    # Turns where the agent only fires a tool call have message=None,
    # hence the guard.
    agent_turns = [
        t.message for t in conversation.transcript if t.role == "agent" and t.message
    ]
    agent_text = " ".join(agent_turns).lower()

    passed = 0
    total = 0

    for slot, needles in REQUIRED_SLOTS.items():
        total += 1
        ok = any(n in agent_text for n in needles)
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] slot: {slot}")

    for phrase in FORBIDDEN_PHRASES:
        total += 1
        ok = phrase not in agent_text
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] forbidden phrase absent: {phrase!r}")

    total += 1
    runs = [m.group() for turn in agent_turns for m in DIGIT_RUN.finditer(turn)]
    ok = not runs
    passed += ok
    tail = f" (found: {', '.join(runs)})" if runs else ""
    print(f"[{'PASS' if ok else 'FAIL'}] digit read-back: no 4+ digit runs{tail}")

    print("-" * 40)
    print(f"{passed}/{total} checks passed ({len(agent_turns)} agent turns scored)")
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()

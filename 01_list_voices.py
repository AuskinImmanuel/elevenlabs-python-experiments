"""List voices available in the ElevenLabs workspace.

Smoke test for the env + key + SDK install.
"""

import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs


def main() -> None:
    load_dotenv()
    api_key = os.environ["ELEVENLABS_API_KEY"]
    client = ElevenLabs(api_key=api_key)

    voices = client.voices.get_all()

    print(f"{'NAME':<30} {'VOICE_ID':<24} CATEGORY")
    print("-" * 70)
    for v in voices.voices:
        print(f"{v.name:<30} {v.voice_id:<24} {v.category or ''}")


if __name__ == "__main__":
    main()

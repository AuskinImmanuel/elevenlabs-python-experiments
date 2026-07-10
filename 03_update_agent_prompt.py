"""Update an existing agent's system prompt without recreating it.

Usage:
    python 03_update_agent_prompt.py <agent_id> <prompt_file>

Sends a partial conversation_config carrying only the new prompt text.
The SDK leaves unset fields out of the PATCH body, so the agent's voice,
LLM, and everything else stay exactly as they were. Verified by dumping
the request body with the SDK's own encoder; see notes/learnings.md.
"""

import os
import sys

from dotenv import load_dotenv
from elevenlabs import AgentConfig, ConversationalConfig
from elevenlabs.client import ElevenLabs
from elevenlabs.types import PromptAgentApiModelOutput


def main() -> None:
    if len(sys.argv) != 3:
        print("usage: python 03_update_agent_prompt.py <agent_id> <prompt_file>")
        sys.exit(1)

    agent_id, prompt_path = sys.argv[1], sys.argv[2]

    load_dotenv()
    api_key = os.environ["ELEVENLABS_API_KEY"]
    client = ElevenLabs(api_key=api_key)

    with open(prompt_path) as f:
        prompt = f.read()

    config = ConversationalConfig(
        agent=AgentConfig(prompt=PromptAgentApiModelOutput(prompt=prompt))
    )

    updated = client.conversational_ai.agents.update(
        agent_id,
        conversation_config=config,
    )

    print(f"updated: {updated.agent_id} ({updated.name})")
    if updated.version_id:
        print(f"version: {updated.version_id}")


if __name__ == "__main__":
    main()

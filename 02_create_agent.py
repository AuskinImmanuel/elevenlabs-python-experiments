"""Create an agent programmatically from a prompt file.

Reads scenarios/card_dispute.md, creates an agent over the API, and
prints the new agent_id. Verify it in the ElevenLabs dashboard after.

SDK note (v2.x): the agents surface lives at client.conversational_ai.agents,
and the prompt nests inside conversation_config.agent.prompt.prompt. The
prompt field is typed with the Output model even on create; the Input model
gets rejected by validation. See notes/learnings.md.
"""

import os

from dotenv import load_dotenv
from elevenlabs import AgentConfig, ConversationalConfig
from elevenlabs.client import ElevenLabs
from elevenlabs.types import PromptAgentApiModelOutput


def main() -> None:
    load_dotenv()
    api_key = os.environ["ELEVENLABS_API_KEY"]
    client = ElevenLabs(api_key=api_key)

    with open("scenarios/card_dispute.md") as f:
        prompt = f.read()

    config = ConversationalConfig(
        agent=AgentConfig(
            first_message="Hi, you've reached card services. How can I help?",
            language="en",
            prompt=PromptAgentApiModelOutput(
                prompt=prompt,
                llm="gemini-2.0-flash",
                temperature=0.3,
            ),
        )
    )

    agent = client.conversational_ai.agents.create(
        name="card-dispute-sandbox",
        conversation_config=config,
    )

    print(f"agent_id: {agent.agent_id}")


if __name__ == "__main__":
    main()

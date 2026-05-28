"""Same prompt, different LLM backends. Log latency and output side-by-side.

Status: stub.

Plan:
  - Take one prompt and a fixed user turn
  - Run against GPT-4.1-mini, Gemini Flash, Claude Haiku
  - Time each call, log token counts, dump outputs to a comparable table
  - Useful for the kind of LLM-swap decisions I make at work but currently delegate
"""


def main() -> None:
    raise NotImplementedError("Pending: multi-provider client setup")


if __name__ == "__main__":
    main()

# Extension — Ask Your Inventory

**Optional, untested, and it costs a little money.** This page connects an AI model to the `shots.json` your project saved, so you can ask questions in plain language: "Which shot is incomplete?", "How many frames does SH020 have?" It uses OpenAI's API with **your own API key**, and OpenAI charges your account for each question, usually a fraction of a cent with the small model below. Skip it if you don't want an account or a bill; Module 0 is complete without it.

## The rule: code produces the facts, the model reports them

A language model can sound confident about things that aren't true. So it never looks at the folder and never counts frames. Your Shot Inventory code produced the facts; the model only reads `shots.json` and answers from it. If the answer isn't in the file, it must say so.

## Your API key is a password

1. Create an account and an API key on the [OpenAI platform](https://platform.openai.com/api-keys), and set a low monthly spending limit in its billing settings.
2. Put the key in an **environment variable** for the current terminal, never in a file in your project:

    ```console
    export OPENAI_API_KEY="your key here"
    ```

    In PowerShell: `$env:OPENAI_API_KEY = "your key here"`.

3. Never write the key in code, commit it, paste it in an issue, or print it. Your fork is public: anything you commit, anyone can read. If a key leaks, delete it on the platform's API keys page at once and create a new one.

## The script

Create a folder `work` in your `module-0` folder and save this in it as `ask.py`:

```python
"""Ask questions about shots.json; the model answers only from the file."""
import json
import sys
from pathlib import Path

from openai import OpenAI

INSTRUCTIONS = (
    "You answer questions about a visual-effects shot inventory. "
    "Use only the JSON you are given. If the answer is not in it, say you don't know."
)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: ask.py SHOTS_JSON QUESTION", file=sys.stderr)
        return 2
    inventory = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    client = OpenAI()  # reads OPENAI_API_KEY from the environment
    response = client.responses.create(
        model="gpt-5.4-nano",
        instructions=INSTRUCTIONS,
        input=f"Inventory:\n{json.dumps(inventory, indent=2)}\n\nQuestion: {argv[1]}",
    )
    print(response.output_text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

Run it with the OpenAI library added for this one command, so the course project's own dependencies stay unchanged:

```console
uv run --with openai python work/ask.py shots.json "Which shot is incomplete, and which frame is missing?"
```

`gpt-5.4-nano` is a small, low-cost model at the time of writing. Model names change; check OpenAI's [models page](https://platform.openai.com/docs/models) and pick its smallest current model if this one is gone.

## Try to make it wrong

Ask a question the file can't answer, such as "Who rendered SH010?" A good answer says the inventory doesn't say. Then ask about a frame number that isn't in the file. When the model guesses instead of refusing, that's the risk the rule above exists for, and the reason a pipeline tool lets code, not a model, produce its facts.

## Further reading

- [OpenAI Python library](https://github.com/openai/openai-python) (OpenAI): installation and the Responses API.
- [Models](https://platform.openai.com/docs/models) (OpenAI): current model names and their prices.

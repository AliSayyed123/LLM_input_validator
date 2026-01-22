import json
import sys
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

from prompts import VALIDATION_PROMPT

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

if not API_KEY:
    print("ERROR: OPENAI_API_KEY not set")
    sys.exit(1)

client = OpenAI(api_key=API_KEY)


def load_input(path: str) -> dict:
    """Read input JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def call_llm(input_data: dict, retries: int = 3):
    """Send data to LLM and enforce structured output."""
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": VALIDATION_PROMPT},
                    {"role": "user", "content": json.dumps(input_data)}
                ],
                temperature=0
            )

            content = response.choices[0].message.content
            parsed = json.loads(content)

            # Schema enforcement ONLY
            assert isinstance(parsed["is_valid"], bool)
            assert isinstance(parsed["errors"], list)
            assert isinstance(parsed["warnings"], list)

            return parsed

        except Exception as e:
            if attempt == retries - 1:
                raise RuntimeError("LLM failed to return valid structured output") from e
            time.sleep(0.5)


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_user.py input.json")
        sys.exit(1)

    input_file = sys.argv[1]
    data = load_input(input_file)
    result = call_llm(data)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

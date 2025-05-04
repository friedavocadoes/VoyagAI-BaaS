import re
import json

def json_parser(response_text):
    # Step 1: Strip markdown-style code blocks
    cleaned = re.sub(r"```(?:json)?", "", response_text)  # remove ```json or ```
    cleaned = cleaned.replace("```", "").strip()

    # Step 2: Remove escaped newlines
    cleaned = cleaned.replace("\\n", "").replace("\\", "")

    # Step 3: Try parsing JSON
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)
        return None

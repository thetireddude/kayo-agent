import os
import sys
from dotenv import load_dotenv
from google import genai
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key = api_key)

parser = argparse.ArgumentParser(description="Kayo Coding Agent")
parser.add_argument("user_prompt", type=str, help="User input prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`
prompt = args.user_prompt

def getResponse(content):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=content
    )
    return response

response = getResponse(prompt)

print(f"Prompt:\n{prompt}")
print(f"\nInput tokens: {response.usage_metadata.prompt_token_count}")
print(f"\nResponse tokens: {response.usage_metadata.candidates_token_count}")
print(f"\nResponse text:\n{response.text}")

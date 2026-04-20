import os
import sys
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key = api_key)

parser = argparse.ArgumentParser(description="Kayo Coding Agent")
parser.add_argument("user_prompt", type=str, help="User input prompt")
parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
args = parser.parse_args()

# Now we can access `args.user_prompt`
prompt = args.user_prompt
verbose = args.verbose

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def getResponse():
    response = client.models.generate_content(
        model="gemma-4-31b-it", contents=messages
    )
    return response


response = getResponse()

if verbose:
    print(f"Prompt:\n{prompt}")
    print(f"\nInput tokens: {response.usage_metadata.prompt_token_count}")
    print(f"\nResponse tokens: {response.usage_metadata.candidates_token_count}")
    print(f"\nResponse text:\n{response.text}")
else:
    print(response.text)

# list all models available via the gemini api
# for model in client.models.list():
#     print(model.name)

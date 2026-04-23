import os
import sys
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from call_function import available_functions
from call_function import call_function

def main():
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
            model="gemma-4-31b-it", 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
                )
        )
        return response

    try:
        response = getResponse()
    except Exception as e:
        print(f'Error: getResponse(): {e}')
        return

    function_call_responses = []

    if verbose:
        print(f"Prompt:\n{prompt}\n")
        # print(f"System Prompt:\n{system_prompt}")
        print(f"Input tokens: {response.usage_metadata.prompt_token_count}\n")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n")

    if response.function_calls:
        if len(response.function_calls) != 0:
            for function_call in response.function_calls:
                # print(f'function call: {function_call}')

                function_call_response = call_function(function_call)

                if not function_call_response.parts:
                    raise Exception 
                if not function_call_response.parts[0].function_response:
                    raise Exception
                if not function_call_response.parts[0].function_response.response:
                    raise Exception

                function_call_responses.append(function_call_response.parts[0])

                if verbose:
                    print(f"-> {function_call_response.parts[0].function_response.response}\n")

    print(f"Response text:\n - {response.text}")

    # list all models available via the gemini api
    # for model in client.models.list():
    #     print(model.name)

if __name__ == "__main__":
    main()

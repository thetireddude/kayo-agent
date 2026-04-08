import os
import argparse
from dotenv import load_dotenv
from google import genai

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.markdown import Markdown

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=api_key)


def getResponse(content):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=content
    )
    return response


def show_welcome(console: Console):
    bg = "#5D4E60"
    border = "#826C7F"
    accent = "#A88FAC"
    light = "#D4B2D8"

    title = Text("Kayo Coding Agent", style=f"bold {light}")
    subtitle = Text("Interactive mode — type 'exit' or '/exit' to quit", style=accent)
    body = Text.assemble(title, "\n", subtitle)
    panel = Panel(Align.center(body), border_style=border, style=f"on {bg}")
    console.print(panel)


def print_response(prompt: str, response, console: Console):
    console.rule("[bold]Response[/bold]")
    console.print(f"[bold]Prompt:[/bold] {prompt}\n")
    console.print(f"[bold]Input tokens:[/bold] {response.usage_metadata.prompt_token_count}")
    console.print(f"[bold]Response tokens:[/bold] {response.usage_metadata.candidates_token_count}\n")
    console.print(Markdown(response.text), soft_wrap=True)    
    console.rule()


def interactive_loop(console: Console):
    accent = "#A88FAC"
    prompt_style = f"bold {accent}"
    while True:
        try:
            user = console.input(f"[{prompt_style}]> [/{prompt_style}]").strip()
        except (KeyboardInterrupt, EOFError):
            console.print()
            break
        if not user:
            continue
        if user.lower() in ("exit", "/exit"):
            break
        response = getResponse(user)
        print_response(user, response, console)


def main():
    parser = argparse.ArgumentParser(description="Kayo Coding Agent")
    parser.add_argument("-i", "--interactive", action="store_true", help="Start interactive REPL")
    parser.add_argument("user_prompt", nargs="?", default=None, help="Single prompt (non-interactive)")
    parser.add_argument("user_help", action="store_true", help="Program help")
    args = parser.parse_args()

    console = Console()
    if args.interactive:
        show_welcome(console)
        interactive_loop(console)
    elif args.user_prompt:
        response = getResponse(args.user_prompt)
        print_response(args.user_prompt, response, console)
    elif args.user_help:
        parser.print_help()     # argparse in-built function


if __name__ == "__main__":
    main()

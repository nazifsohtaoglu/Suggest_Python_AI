import os
from urllib import response
import openai
import argparse

MAX_INPUT_LENGTH = 40

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    input = args.input
    if check_length(input):
        result = generate_suggestion(input)
        print(result)
    else:
        raise ValueError("This is too long. It must be  under {MAX_INPUT_LENGTH} char")


def check_length(prompt: str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH


def generate_suggestion(prompt: str):

    openai.organization = "org-Z8YoasqcZXbY9eE3C9p3XRvb"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    argument = f"Suggest me a good {prompt}"
    response = openai.Completion.create(
        engine="text-davinci-002", prompt=argument, max_tokens=32)

    suggestion: str = response["choices"][0]["text"]
    suggestion = suggestion.strip()

    last = suggestion[-1]
    if last not in {".", "!", "?"}:
        suggestion += "..."
    return suggestion


if __name__ == "__main__":
    main()

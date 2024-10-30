import google.generativeai as genai 

def print_model_information(model_name):
    # Returns the "context window" for the model, which is the combined input and output token limits.
    model_info = genai.get_model(f"models/{model_name}")
    input_token_limit= model_info.input_token_limit
    output_token_limit = model_info.output_token_limit
    print(f"{input_token_limit=}")
    print(f"{output_token_limit=}")
    return input_token_limit, output_token_limit

with open('gemini-api-key.txt', 'r') as f:
    api_key = f.read().strip()

genai.configure(api_key=api_key)
model_name ="gemini-pro"
model = genai.GenerativeModel(model_name)
print_model_information(model_name)

question = """Summarize this text: 
In this chapter, we’ll focus on interacting with Linux on the terminal, that is, via the
shell that exposes a command-line interface (CLI). It is vitally important to be able to
use the shell effectively to accomplish everyday tasks, and to that end we focus on
usability here.

First, we review some terminology and provide a gentle and concise introduction to
shell basics. Then we have a look at modern, human-friendly shells, such as the Fish
shell. We’ll also look at configuration and common tasks in the shell. Then, we move
on to the topic of how to effectively work on the CLI using a terminal multiplexer,
enabling you to work with multiple sessions, local or remote. In the last part of this
chapter, we switch gears and focus on automating tasks in the shell using scripts,
including best practices for writing scripts in a safe, secure, and portable manner and
also how to lint and test scripts.

There are two major ways to interact with Linux, from a CLI perspective. The first
way is manually—that is, a human user sits in front of the terminal, interactively typ‐
ing commands and consuming the output. This ad-hoc interaction works for most of
the things you want to do in the shell on a day-to-day basis, including the following:
"""

# Call `count_tokens` to get the input token count (`total_tokens`).
print("total_tokens: ", model.count_tokens(question))
response = model.generate_content(f"{question}")
answer = response.text
print(question)
print("-------------------------------------\n")
print(answer)
print(response.usage_metadata)




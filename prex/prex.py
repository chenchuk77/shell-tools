#!/usr/bin/python

import os
import json
import requests

# Fetch PREX_SERVER_HOST and PREX_SERVER_PORT from environment variables
PREX_SERVER_HOST = os.getenv("PREX_SERVER_HOST")
PREX_SERVER_PORT = os.getenv("PREX_SERVER_PORT")
PREX_HOME = os.getenv("PREX_HOME")

# Check if PREX_SERVER_HOST and PREX_SERVER_PORT are set
if PREX_HOME is None or PREX_SERVER_HOST is None or PREX_SERVER_PORT is None:
    print("Error: PREX_HOME/PREX_SERVER_HOST/PREX_SERVER_PORT environment variables must be set.")
    exit(1)

script_dir = os.path.dirname(os.path.abspath(__file__))
#prompts_file = os.path.join(script_dir, "prompts.json")
prompts_file = os.path.join(PREX_HOME, "prompts.json")

def save_prompt(user, reply):
    with open(prompts_file, "r") as f:
        data = json.load(f)
    new_object = {"user": f"{user}", "reply": f"{reply}"}
    data["prompts"].append(new_object)
    with open(prompts_file, "w") as f:
        json.dump(data, f, indent=2)

def prompt_extender(prompt):
    url = f"http://{PREX_SERVER_HOST}:{PREX_SERVER_PORT}/prompt"
    data = {"prompt_req": prompt}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        reply = response.json()["prompt_reply"]
        print(reply)
        save_prompt(prompt, reply)
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    import sys
    prompt = sys.argv[1]  # Get the prompt from the first command-line argument
    prompt_extender(prompt)


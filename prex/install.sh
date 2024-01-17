#!/bin/bash

# Script to install 'prex.python'

PREX_HOME="$HOME/shell-utils/prex"

# Define the source and target paths
SOURCE_SCRIPT="$PREX_HOME/prex.py"
TARGET_LINK="$HOME/.local/bin/prex"
PROMPTS_FILE="$PREX_HOME/prompts.json"

# Check for the existence of prompts.json, create if not exists
if [[ ! -f "$PROMPTS_FILE" ]]; then
    echo -e "{\n  \"prompts\": [\n  ]\n}" > "$PROMPTS_FILE"
    echo "Created prompts.json in the script directory."
fi

# Check if the target link already exists
if [[ -L "$TARGET_LINK" ]] || [[ -f "$TARGET_LINK" ]]; then
    echo "prex already installed."
    echo "usage:"
    echo "prex \"big blue car\""
    echo ""
    echo "big blue car with legs in a parking lot, concept art  by Justin Gerard, trending on artstation, cgsociety, speedpainting, official art, poster art, 8k.  ambient occlusion. bokeh. cinematic lighting.  film photograph, 180mm"
    echo""

else
    # Create a symlink in /usr/local/bin
    ln -s "$SOURCE_SCRIPT" "$TARGET_LINK"
    chmod +x "$SOURCE_SCRIPT"
    echo "prex installed."
fi

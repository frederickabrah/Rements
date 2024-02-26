#!/bin/bash

#install the neccesary commands
apt install python3 && apt install python3.11-venv

#install requirement.txt
pip install -r requirement.txt

# Create a virtual environment
python3 -m venv dos_attacker_env

# Activate the virtual environment
source dos_attacker_env/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Run the DoS attack tool
python dos_attack_tool.py

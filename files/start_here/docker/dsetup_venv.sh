#!/bin/bash

# Check if Python 3.12 is installed
if ! python3.12 --version &>/dev/null; then
  echo "Python 3.12 is not installed. Please install Python 3.12 and try again."
  exit 1
fi

# Create a virtual environment
python3.12 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install necessary libraries
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate

echo "Virtual environment setup complete. To activate, run 'source venv/bin/activate'."

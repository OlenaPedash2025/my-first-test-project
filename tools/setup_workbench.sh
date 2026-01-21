#!/bin/bash

# This script sets up a development environment in the current directory
echo "--- Starting Workbench Setup in: $(pwd) ---"

# 1. Python Virtual Environment Setup
echo "Creating Python virtual environment (.venv)..."
python3 -m venv .venv

# Activate the environment to install packages
# Note: This only activates it for the duration of this script
source .venv/bin/activate

# Upgrade pip (the package installer)
echo "Upgrading pip..."
pip install --upgrade pip

# Check for requirements.txt and install libraries
if [ -f "requirements.txt" ]; then
    echo "Installing Python libraries from requirements.txt..."
    pip install -r requirements.txt
else
echo "No requirements.txt found. Creating a blank one."
    touch requirements.txt
fi

# 2. Node.js & TypeScript Setup
echo -e "\n--- Setting up Node.js & TypeScript ---"
if [ ! -f "package.json" ]; then
    echo "Initializing npm..."
    npm init -y
fi

echo "Installing TypeScript and essential types..."
npm install typescript ts-node @types/node --save-dev

# 3. TypeScript Initialization
if [ ! -f "tsconfig.json" ]; then
    echo "Creating tsconfig.json..."
    npx tsc --init
fi

# 4. Git Configuration (.gitignore)
echo -e "\n--- Checking .gitignore ---"
if [ ! -f ".gitignore" ]; then
    echo "Creating .gitignore to exclude environment files..."
    cat <<EOT >> .gitignore
.venv/
node_modules/
__pycache__/
*.js
.DS_Store
EOT
    echo ".gitignore created successfully."
fi

echo -e "\n✅ ALL DONE!"
echo "------------------------------------------------"
echo "To start working, run: source .venv/bin/activate"
echo "Then you can verify installations with: pip list"
echo "------------------------------------------------"
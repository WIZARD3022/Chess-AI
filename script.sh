#!/bin/bash

# Activate the virtual environment
source myenv/Scripts/activate

# Run the Python script
python main.py


# Default commit message or use the one from argument
COMMIT_MSG=${1:-"Auto commit"}

echo "Adding all files..."
git add .
git rm --cached script.sh
# git rm --cached myenv
# git reset script.sh

echo "Committing with message: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

echo "Pushing to GitHub..."
git push origin main


# Confirm execution
echo "Done"

#!/bin/sh

session_file="${SESSION_NAME}.session"

if [ "$1" = "--auth" ]; then
  echo "Starting authentication process with --auth..."
  python3 main.py --auth
elif [ -f "$session_file" ]; then
  echo "Session file found, running bot without --auth..."
  python3 main.py
else
  echo "Session file not found. Please authenticate first with --auth arg."
  echo "Run the following command to authenticate:"
  echo "docker compose run app --auth"
  exit 1
fi
#!/usr/bin/env bash
set -euo pipefail

BOARD="/Volumes/CIRCUITPY"

if [ ! -d "$BOARD" ]; then
  echo "CIRCUITPY drive not found at $BOARD"
  exit 1
fi

cp code.py "$BOARD/code.py"

mkdir -p "$BOARD/lib"
if [ -d "lib" ]; then
  cp -R lib/* "$BOARD/lib/" 2>/dev/null || true
fi

echo "Deployed to CIRCUITPY"
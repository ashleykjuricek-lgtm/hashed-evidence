#!/bin/bash
# hashEvidence — Hash, commit, push, and create next folder
# Usage: ./hashEvidence.sh
# Just drop files in the latest numbered folder and run this.

cd "$(dirname "$0")" || exit 1

# Find the highest numbered folder
CURRENT=$(ls -d [0-9][0-9][0-9] 2>/dev/null | sort -n | tail -1)

if [ -z "$CURRENT" ]; then
  echo "ERROR: No numbered folder found. Creating 001 for you."
  mkdir 001
  echo "Drop your evidence files in 001/ and run this again."
  exit 1
fi

# Check if folder has files (besides hashes.txt)
FILE_COUNT=$(find "$CURRENT" -maxdepth 1 -type f ! -name "hashes.txt" | wc -l | tr -d ' ')

if [ "$FILE_COUNT" -eq 0 ]; then
  echo "Folder $CURRENT/ is empty. Drop your evidence files there first."
  exit 1
fi

echo "=== hashEvidence ==="
echo "Sealing folder: $CURRENT/"
echo ""

# Hash every file
echo "# SHA-256 hashes — sealed $(date -u +"%Y-%m-%d %H:%M:%S UTC")" > "$CURRENT/hashes.txt"
echo "" >> "$CURRENT/hashes.txt"

for f in "$CURRENT"/*; do
  BASENAME=$(basename "$f")
  [ "$BASENAME" = "hashes.txt" ] && continue
  [ ! -s "$f" ] && continue
  HASH=$(shasum -a 256 "$f" | awk '{print $1}')
  printf "%-60s %s\n" "$BASENAME" "$HASH" >> "$CURRENT/hashes.txt"
  echo "  HASHED: $BASENAME"
done

echo ""

# Git add, commit, push
git add "$CURRENT/"
git commit -m "Seal evidence $CURRENT — $(date +"%Y-%m-%d %H:%M")"
git push

echo ""

# Create next folder
NEXT=$(printf "%03d" $((10#$CURRENT + 1)))
mkdir -p "$NEXT"

echo "=== DONE ==="
echo "Sealed:  $CURRENT/"
echo "Next:    $NEXT/ (ready for your next evidence drop)"

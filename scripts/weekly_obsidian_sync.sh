#!/bin/bash
# Weekly Obsidian sync script
# Syncs screenshots, AI chats, and Copy to Obsidian folder

VAULT_PATH="/Users/KevinHG/Documents/HG Main"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_FILE="$HOME/.obsidian_sync_log.txt"

echo "======================================" >> "$LOG_FILE"
echo "Obsidian Sync - $(date)" >> "$LOG_FILE"
echo "======================================" >> "$LOG_FILE"

# Sync Screenshots (last 7 days)
echo "Syncing screenshots..." >> "$LOG_FILE"
python3 "$SCRIPT_DIR/organize_screenshots.py" 7 >> "$LOG_FILE" 2>&1

# Sync AI Chat Exports (last 7 days)
echo "Syncing AI chat exports..." >> "$LOG_FILE"
python3 "$SCRIPT_DIR/organize_ai_chats.py" 7 >> "$LOG_FILE" 2>&1

# Convert new CMUX chats
echo "Converting CMUX chats..." >> "$LOG_FILE"
python3 "$SCRIPT_DIR/cmux_jsonl_converter.py" >> "$LOG_FILE" 2>&1

# Sync "Copy to Obsidian" folder
COPY_TO_OBSIDIAN="/Users/KevinHG/Desktop/Copy to Obsidian"
if [ -d "$COPY_TO_OBSIDIAN" ]; then
    echo "Syncing Copy to Obsidian folder..." >> "$LOG_FILE"
    # Copy everything from this folder to vault root, preserving structure
    rsync -av --update "$COPY_TO_OBSIDIAN/" "$VAULT_PATH/" >> "$LOG_FILE" 2>&1
fi

# Sync the staging folder (Copy to HG Main)
STAGING_FOLDER="/Users/KevinHG/Documents/Copy to HG Main (weekly cron job)"
if [ -d "$STAGING_FOLDER" ]; then
    echo "Syncing staging folder..." >> "$LOG_FILE"
    # Look for new files added in last 7 days
    find "$STAGING_FOLDER" -type f -mtime -7 | while read file; do
        # Determine relative path
        rel_path="${file#$STAGING_FOLDER/}"
        target="$VAULT_PATH/$rel_path"
        target_dir=$(dirname "$target")
        
        # Create target directory
        mkdir -p "$target_dir"
        
        # Copy if newer or doesn't exist
        if [ ! -f "$target" ] || [ "$file" -nt "$target" ]; then
            cp "$file" "$target"
            echo "  Copied: $rel_path" >> "$LOG_FILE"
        fi
    done
fi

echo "Sync complete: $(date)" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

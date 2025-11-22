#!/bin/bash
# Copy Obsidian plugins and settings between vaults

SOURCE_VAULT="$1"
TARGET_VAULT="$2"

if [ -z "$SOURCE_VAULT" ] || [ -z "$TARGET_VAULT" ]; then
    echo "Usage: $0 <source_vault> <target_vault>"
    echo ""
    echo "Example:"
    echo "  $0 '/Users/KevinHG/Documents/HG Main Big Mac' '/Users/KevinHG/Documents/HG Main'"
    exit 1
fi

SOURCE_OBSIDIAN="$SOURCE_VAULT/.obsidian"
TARGET_OBSIDIAN="$TARGET_VAULT/.obsidian"

if [ ! -d "$SOURCE_OBSIDIAN" ]; then
    echo "Error: Source .obsidian folder not found: $SOURCE_OBSIDIAN"
    exit 1
fi

if [ ! -d "$TARGET_OBSIDIAN" ]; then
    echo "Creating target .obsidian folder..."
    mkdir -p "$TARGET_OBSIDIAN"
fi

echo "Copying Obsidian settings and plugins..."
echo "Source: $SOURCE_VAULT"
echo "Target: $TARGET_VAULT"
echo ""

# Backup existing target settings
if [ -d "$TARGET_OBSIDIAN" ]; then
    BACKUP_DIR="$TARGET_VAULT/.obsidian.backup.$(date +%Y%m%d_%H%M%S)"
    echo "Creating backup: $BACKUP_DIR"
    cp -R "$TARGET_OBSIDIAN" "$BACKUP_DIR"
fi

# Copy core settings
echo "✓ Copying core settings..."
cp "$SOURCE_OBSIDIAN/app.json" "$TARGET_OBSIDIAN/" 2>/dev/null || echo "  (app.json not found)"
cp "$SOURCE_OBSIDIAN/appearance.json" "$TARGET_OBSIDIAN/" 2>/dev/null || echo "  (appearance.json not found)"
cp "$SOURCE_OBSIDIAN/community-plugins.json" "$TARGET_OBSIDIAN/" 2>/dev/null || echo "  (community-plugins.json not found)"
cp "$SOURCE_OBSIDIAN/core-plugins.json" "$TARGET_OBSIDIAN/" 2>/dev/null || echo "  (core-plugins.json not found)"
cp "$SOURCE_OBSIDIAN/hotkeys.json" "$TARGET_OBSIDIAN/" 2>/dev/null || echo "  (hotkeys.json not found)"
cp "$SOURCE_OBSIDIAN/workspace.json" "$TARGET_OBSIDIAN/" 2>/dev/null || echo "  (workspace.json not found)"

# Copy plugins folder
if [ -d "$SOURCE_OBSIDIAN/plugins" ]; then
    echo "✓ Copying plugins folder..."
    cp -R "$SOURCE_OBSIDIAN/plugins" "$TARGET_OBSIDIAN/"
    
    # Count plugins
    PLUGIN_COUNT=$(ls -1 "$TARGET_OBSIDIAN/plugins" | wc -l | tr -d ' ')
    echo "  Copied $PLUGIN_COUNT plugins"
fi

# Copy themes
if [ -d "$SOURCE_OBSIDIAN/themes" ]; then
    echo "✓ Copying themes folder..."
    cp -R "$SOURCE_OBSIDIAN/themes" "$TARGET_OBSIDIAN/"
fi

# Copy snippets
if [ -d "$SOURCE_OBSIDIAN/snippets" ]; then
    echo "✓ Copying snippets folder..."
    cp -R "$SOURCE_OBSIDIAN/snippets" "$TARGET_OBSIDIAN/"
fi

# Copy Smart Connections environment
if [ -d "$SOURCE_VAULT/.smart-env" ]; then
    echo "✓ Copying Smart Connections environment..."
    cp -R "$SOURCE_VAULT/.smart-env" "$TARGET_VAULT/"
fi

echo ""
echo "============================================================"
echo "Copy complete!"
echo "Backup saved to: $BACKUP_DIR"
echo "Restart Obsidian to apply changes"
echo "============================================================"

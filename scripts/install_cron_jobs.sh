#!/bin/bash
# Install weekly cron jobs for Obsidian sync

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SYNC_SCRIPT="$SCRIPT_DIR/weekly_obsidian_sync.sh"

echo "Obsidian Sync - Cron Job Installer"
echo "===================================="
echo ""
echo "This will install a weekly cron job that runs every Sunday at 9 AM."
echo "The job will sync:"
echo "  • Screenshots (last 7 days)"
echo "  • AI Chat Exports (last 7 days)"
echo "  • CMUX conversations"
echo "  • Desktop/Copy to Obsidian folder"
echo "  • Copy to HG Main staging folder"
echo ""
echo "Script location: $SYNC_SCRIPT"
echo ""

# Check if script exists
if [ ! -f "$SYNC_SCRIPT" ]; then
    echo "Error: Sync script not found at $SYNC_SCRIPT"
    exit 1
fi

# Check for existing cron job
EXISTING_CRON=$(crontab -l 2>/dev/null | grep "weekly_obsidian_sync.sh")

if [ ! -z "$EXISTING_CRON" ]; then
    echo "⚠️  Cron job already installed:"
    echo "   $EXISTING_CRON"
    echo ""
    read -p "Do you want to reinstall? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled."
        exit 0
    fi
    
    # Remove existing job
    crontab -l 2>/dev/null | grep -v "weekly_obsidian_sync.sh" | crontab -
    echo "✓ Removed existing cron job"
fi

# Create new cron job
# Format: minute hour day_of_month month day_of_week command
# 0 9 * * 0 = Every Sunday at 9:00 AM
CRON_LINE="0 9 * * 0 $SYNC_SCRIPT"

# Add to crontab
(crontab -l 2>/dev/null; echo "$CRON_LINE") | crontab -

echo ""
echo "✓ Cron job installed successfully!"
echo ""
echo "Schedule: Every Sunday at 9:00 AM"
echo "Command: $SYNC_SCRIPT"
echo ""
echo "To view your cron jobs:"
echo "  crontab -l"
echo ""
echo "To manually run the sync now:"
echo "  $SYNC_SCRIPT"
echo ""
echo "To check the sync log:"
echo "  cat ~/.obsidian_sync_log.txt"
echo ""

# Ask if user wants to run now
read -p "Do you want to run the sync now as a test? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Running sync..."
    echo ""
    "$SYNC_SCRIPT"
    echo ""
    echo "Check the log for details:"
    echo "  tail -50 ~/.obsidian_sync_log.txt"
fi

echo ""
echo "Installation complete!"

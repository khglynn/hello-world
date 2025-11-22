#!/bin/bash
# Uninstall Obsidian sync cron jobs

echo "Obsidian Sync - Cron Job Uninstaller"
echo "====================================="
echo ""

# Check for existing cron job
EXISTING_CRON=$(crontab -l 2>/dev/null | grep "weekly_obsidian_sync.sh")

if [ -z "$EXISTING_CRON" ]; then
    echo "No Obsidian sync cron job found."
    exit 0
fi

echo "Found cron job:"
echo "  $EXISTING_CRON"
echo ""

read -p "Do you want to remove this cron job? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Uninstallation cancelled."
    exit 0
fi

# Remove the job
crontab -l 2>/dev/null | grep -v "weekly_obsidian_sync.sh" | crontab -

echo "✓ Cron job removed successfully!"
echo ""
echo "The sync scripts are still available in:"
echo "  $(cd "$(dirname "$0")" && pwd)"
echo ""
echo "You can reinstall anytime by running:"
echo "  ./install_cron_jobs.sh"

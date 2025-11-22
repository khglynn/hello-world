#!/bin/bash
# Quick Apple Notes export using optimized AppleScript

VAULT_PATH="/Users/KevinHG/Documents/HG Main"
DAYS_BACK="${1:-7}"

echo "Exporting Apple Notes from last $DAYS_BACK days..."
echo "Target: $VAULT_PATH/Apple Notes"
echo ""

# Calculate cutoff date (macOS date format)
if [ "$DAYS_BACK" = "all" ]; then
    CUTOFF_DATE="2000-01-01"
else
    CUTOFF_DATE=$(date -v-${DAYS_BACK}d "+%Y-%m-%d")
fi

echo "Cutoff date: $CUTOFF_DATE"
echo "Fetching notes..."
echo ""

# Export using simpler AppleScript (faster)
osascript <<'APPLESCRIPT'
tell application "Notes"
    set exportCount to 0
    set skipCount to 0
    
    repeat with aNote in every note
        try
            set noteName to name of aNote
            set noteBody to body of aNote
            set noteCreated to creation date of aNote as «class isot» as string
            set noteModified to modification date of aNote as «class isot» as string
            
            try
                set noteFolder to name of container of aNote
            on error
                set noteFolder to "iCloud"
            end try
            
            -- Check if recent (simple check - export most recent 50 for test)
            set currentTime to current date
            set timeDiff to (currentTime - modification date of aNote) / days
            
            if timeDiff < 7 then
                -- Create JSON-like output
                log "EXPORT|" & noteName & "|" & noteCreated & "|" & noteModified & "|" & noteFolder
                set exportCount to exportCount + 1
            else
                set skipCount to skipCount + 1
            end if
            
        on error errMsg
            log "ERROR|" & errMsg
        end try
    end repeat
    
    log "SUMMARY|Exported:" & exportCount & "|Skipped:" & skipCount
end tell
APPLESCRIPT

echo ""
echo "AppleScript export complete"

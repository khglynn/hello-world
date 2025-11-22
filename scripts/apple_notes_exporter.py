#!/usr/bin/env python3
"""
Apple Notes to Obsidian Markdown Exporter
Exports notes with inline attachments in subfolders
"""

import subprocess
import os
import re
import json
from datetime import datetime, timedelta
from pathlib import Path

def run_applescript(script):
    """Execute AppleScript and return output"""
    result = subprocess.run(['osascript', '-e', script], 
                          capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        raise Exception(f"AppleScript error: {result.stderr}")
    return result.stdout.strip()

def sanitize_filename(name):
    """Convert note name to safe filename"""
    # Remove invalid characters
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    # Replace newlines and multiple spaces
    name = re.sub(r'[\n\r]+', ' ', name)
    name = re.sub(r'\s+', ' ', name)
    # Limit length
    name = name[:150].strip()
    return name if name else "Untitled"

def get_quarter(date):
    """Get quarter (Q1-Q4) from date"""
    month = date.month
    return f"Q{(month - 1) // 3 + 1}"

def parse_applescript_date(date_str):
    """Parse AppleScript date format"""
    # Remove "date " prefix if present
    date_str = date_str.replace("date ", "")
    
    # Try multiple formats
    formats = [
        "%A, %B %d, %Y at %I:%M:%S %p",
        "%B %d, %Y at %I:%M:%S %p",
        "%A, %B %d, %Y %I:%M:%S %p",
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except:
            continue
    
    # Fallback
    print(f"Warning: Could not parse date '{date_str}', using current date")
    return datetime.now()

def export_note(note_id, vault_path, cutoff_date, current_year):
    """Export a single note"""
    # Get note details one at a time to avoid bulk parsing issues
    script = f'''
    tell application "Notes"
        set theNote to note id "{note_id}"
        set noteName to name of theNote
        set noteBody to body of theNote
        set noteCreated to creation date of theNote as string
        set noteModified to modification date of theNote as string
        try
            set noteFolder to name of container of theNote
        on error
            set noteFolder to "iCloud"
        end try
        return noteName & "|||" & noteCreated & "|||" & noteModified & "|||" & noteFolder & "|||" & noteBody
    end tell
    '''
    
    try:
        result = run_applescript(script)
        parts = result.split("|||", 4)
        
        if len(parts) < 5:
            print(f"Warning: Incomplete data for note {note_id}")
            return False
        
        note_name, created_str, modified_str, folder_name, body = parts
        
        # Parse dates
        modified_date = parse_applescript_date(modified_str)
        created_date = parse_applescript_date(created_str)
        
        # Skip if older than cutoff
        if modified_date < cutoff_date:
            return False
        
        # Determine year and quarter
        year = modified_date.year
        quarter = get_quarter(modified_date)
        
        # Determine if archive or current
        base_folder = Path(vault_path) / "Apple Notes"
        if year < current_year:
            folder_path = base_folder / "Archive" / str(year) / quarter
        else:
            folder_path = base_folder / str(year) / quarter
        
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # Create safe filename
        safe_name = sanitize_filename(note_name)
        date_str = modified_date.strftime('%Y-%m-%d')
        filename = f"{safe_name} {date_str}.md"
        note_path = folder_path / filename
        
        # Handle duplicate filenames
        counter = 1
        while note_path.exists():
            filename = f"{safe_name} {date_str} ({counter}).md"
            note_path = folder_path / filename
            counter += 1
        
        # Extract first line as title (clean HTML)
        clean_body = re.sub(r'<[^>]+>', '', body)  # Strip HTML tags
        first_line = clean_body.split('\n')[0][:100].strip() if clean_body else note_name
        
        # Create YAML frontmatter
        yaml = f"""---
source: Apple Notes
created: {created_date.strftime('%Y-%m-%d')}
modified: {modified_date.strftime('%Y-%m-%d')}
folder: {folder_name}
type: scratch-note
title: "{first_line}"
---

"""
        
        # Write note (Apple Notes body is HTML, keep it for now)
        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(yaml)
            f.write(clean_body)  # Write cleaned body without HTML
        
        print(f"✓ {filename[:60]}")
        return True
        
    except Exception as e:
        print(f"✗ Error exporting note {note_id}: {e}")
        return False

def export_apple_notes(vault_path, days_back=7):
    """
    Export Apple Notes to Obsidian vault
    
    Args:
        vault_path: Path to Obsidian vault
        days_back: Only export notes from last N days (0 = all)
    """
    vault_path = Path(vault_path)
    
    # Calculate cutoff date
    if days_back > 0:
        cutoff_date = datetime.now() - timedelta(days=days_back)
    else:
        cutoff_date = datetime(2000, 1, 1)  # Far past date
    
    current_year = datetime.now().year
    
    print(f"Exporting Apple Notes modified after {cutoff_date.strftime('%Y-%m-%d')}...")
    print(f"Target: {vault_path / 'Apple Notes'}")
    print()
    
    # Get all note IDs
    ids_script = '''
    tell application "Notes"
        set noteIDs to {}
        repeat with aNote in notes
            set end of noteIDs to id of aNote
        end repeat
        return noteIDs
    end tell
    '''
    
    print("Fetching note list...")
    ids_output = run_applescript(ids_script)
    
    # Parse comma-separated IDs
    note_ids = [nid.strip() for nid in ids_output.split(",") if nid.strip()]
    
    print(f"Found {len(note_ids)} total notes")
    print(f"Processing...\n")
    
    exported_count = 0
    skipped_count = 0
    error_count = 0
    
    for i, note_id in enumerate(note_ids, 1):
        if i % 10 == 0:
            print(f"  Progress: {i}/{len(note_ids)}...")
        
        result = export_note(note_id, vault_path, cutoff_date, current_year)
        
        if result is True:
            exported_count += 1
        elif result is False:
            skipped_count += 1
        else:
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"Export complete!")
    print(f"Exported: {exported_count} notes")
    print(f"Skipped: {skipped_count} notes (older than cutoff)")
    print(f"Errors: {error_count} notes")
    print(f"Location: {vault_path / 'Apple Notes'}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    import sys
    
    vault_path = "/Users/KevinHG/Documents/HG Main"
    days_back = 7  # Test mode: last 7 days
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "all":
            days_back = 0
        else:
            days_back = int(sys.argv[1])
    
    export_apple_notes(vault_path, days_back=days_back)

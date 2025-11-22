#!/usr/bin/env python3
"""
Organize AI Chat Exports into Obsidian vault by month
Filters by date and adds YAML properties
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime, timedelta

def extract_date_from_filename(filename):
    """Try to extract date from various filename formats"""
    # Common patterns in exported chat filenames
    patterns = [
        r'(\d{4})-(\d{2})-(\d{2})',  # 2025-11-21
        r'(\d{4})_(\d{2})_(\d{2})',  # 2025_11_21
        r'(\d{2})-(\d{2})-(\d{4})',  # 21-11-2025
        r'(\d{8})',                   # 20251121
    ]
    
    for pattern in patterns:
        match = re.search(pattern, filename)
        if match:
            try:
                groups = match.groups()
                if len(groups) == 3:
                    if len(groups[0]) == 4:  # Year first
                        year, month, day = int(groups[0]), int(groups[1]), int(groups[2])
                    else:  # Day first
                        day, month, year = int(groups[0]), int(groups[1]), int(groups[2])
                    return datetime(year, month, day)
                elif len(groups) == 1 and len(groups[0]) == 8:  # YYYYMMDD
                    date_str = groups[0]
                    return datetime(int(date_str[0:4]), int(date_str[4:6]), int(date_str[6:8]))
            except:
                continue
    
    return None

def extract_date_from_overview(file_path):
    """Extract date from Overview section in exported AI chats"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Look for Created date in Overview section
        # Format: - **Created:** 7/17/2025, 1:13:51 PM
        created_match = re.search(r'\*\*Created:\*\*\s+(\d{1,2}/\d{1,2}/\d{4})', content)
        if created_match:
            date_str = created_match.group(1)
            # Parse M/D/YYYY format
            return datetime.strptime(date_str, '%m/%d/%Y')
    except:
        pass
    return None

def get_file_date(file_path):
    """Get date from file - try Overview, then filename, then modification time"""
    # Try Overview section first (most accurate)
    date = extract_date_from_overview(file_path)
    if date:
        return date
    
    # Try filename
    date = extract_date_from_filename(file_path.name)
    if date:
        return date
    
    # Fall back to file modification time
    mtime = os.path.getmtime(file_path)
    return datetime.fromtimestamp(mtime)

def detect_source_from_path(file_path):
    """Detect AI source from folder name"""
    path_lower = str(file_path).lower()
    
    if 'chatgpt' in path_lower or 'openai' in path_lower:
        return 'ChatGPT'
    elif 'claude' in path_lower or 'anthropic' in path_lower:
        return 'Claude'
    elif 'gemini' in path_lower or 'bard' in path_lower:
        return 'Gemini'
    elif 'copilot' in path_lower or 'bing' in path_lower:
        return 'Copilot'
    elif 'cmux' in path_lower:
        return 'CMUX'
    else:
        return 'Unknown'

def extract_overview_metadata(file_path):
    """Extract metadata from Overview section"""
    metadata = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract various fields from Overview
        # Title
        title_match = re.search(r'\*\*Title:\*\*\s+(.+)', content)
        if title_match:
            metadata['title'] = title_match.group(1).strip()
        
        # URL
        url_match = re.search(r'\*\*Url:\*\*\s+\[([^\]]+)\]', content)
        if url_match:
            metadata['url'] = url_match.group(1)
        
        # ID
        id_match = re.search(r'\*\*ID:\*\*\s+([a-f0-9\-]+)', content)
        if id_match:
            metadata['chat_id'] = id_match.group(1)
        
        # Created date
        created_match = re.search(r'\*\*Created:\*\*\s+(.+)', content)
        if created_match:
            metadata['created'] = created_match.group(1).strip()
        
        # Last Updated
        updated_match = re.search(r'\*\*Last Updated:\*\*\s+(.+)', content)
        if updated_match:
            metadata['last_updated'] = updated_match.group(1).strip()
        
        # Total Messages
        messages_match = re.search(r'\*\*Total Messages:\*\*\s+(\d+)', content)
        if messages_match:
            metadata['message_count'] = int(messages_match.group(1))
            
    except:
        pass
    
    return metadata

def add_yaml_frontmatter(file_path, output_path, source, date):
    """Add YAML frontmatter to markdown file"""
    # Read existing content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if frontmatter already exists
    if content.startswith('---\n'):
        # Already has frontmatter, just copy
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return
    
    # Extract overview metadata
    overview = extract_overview_metadata(file_path)
    
    # Get title (from overview, first heading, or filename)
    if 'title' in overview:
        title = overview['title']
    else:
        lines = content.split('\n')
        title = lines[0].strip('# ').strip() if lines else file_path.stem
    
    if len(title) > 100:
        title = title[:100] + "..."
    
    # Create YAML with all available metadata
    yaml_lines = ['---']
    yaml_lines.append(f'source: {source}')
    yaml_lines.append(f'date: {date.strftime("%Y-%m-%d")}')
    yaml_lines.append(f'title: "{title}"')
    
    if 'chat_id' in overview:
        yaml_lines.append(f'chat_id: {overview["chat_id"]}')
    if 'url' in overview:
        yaml_lines.append(f'url: {overview["url"]}')
    if 'message_count' in overview:
        yaml_lines.append(f'message_count: {overview["message_count"]}')
    if 'created' in overview:
        yaml_lines.append(f'created: "{overview["created"]}"')
    if 'last_updated' in overview:
        yaml_lines.append(f'last_updated: "{overview["last_updated"]}"')
    
    yaml_lines.append('---')
    yaml_lines.append('')
    
    yaml = '\n'.join(yaml_lines)
    
    # Write with frontmatter
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(yaml)
        f.write(content)

def organize_chat_exports(source_dir, vault_path, days_back=7):
    """
    Organize AI chat exports into vault by month
    
    Args:
        source_dir: Source directory with chat exports
        vault_path: Target Obsidian vault
        days_back: Only copy files from last N days (0 = all)
    """
    source_dir = Path(source_dir)
    vault_path = Path(vault_path)
    base_output = vault_path / "AI Chats"
    
    # Calculate cutoff date
    if days_back > 0:
        cutoff_date = datetime.now() - timedelta(days=days_back)
    else:
        cutoff_date = datetime(2000, 1, 1)
    
    print(f"Organizing AI Chat Exports...")
    print(f"Source: {source_dir}")
    print(f"Target: {base_output}")
    print(f"Filter: Files from last {days_back} days (after {cutoff_date.strftime('%Y-%m-%d')})")
    print()
    
    # Find all markdown files
    md_files = list(source_dir.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files")
    print("Processing...\n")
    
    copied_count = 0
    skipped_count = 0
    error_count = 0
    
    for file_path in md_files:
        try:
            # Get file date
            file_date = get_file_date(file_path)
            
            # Skip if older than cutoff
            if file_date < cutoff_date:
                skipped_count += 1
                continue
            
            # Detect source
            source = detect_source_from_path(file_path)
            
            # Determine output folder (monthly)
            year = file_date.year
            month = file_date.strftime('%b')  # Nov, Dec, etc.
            output_dir = base_output / str(year) / month
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Create output filename
            output_filename = f"{source} - {file_path.stem}.md"
            output_path = output_dir / output_filename
            
            # Handle duplicates
            counter = 1
            while output_path.exists():
                output_filename = f"{source} - {file_path.stem} ({counter}).md"
                output_path = output_dir / output_filename
                counter += 1
            
            # Copy with frontmatter
            add_yaml_frontmatter(file_path, output_path, source, file_date)
            
            copied_count += 1
            if copied_count % 10 == 0:
                print(f"  Progress: {copied_count} files copied...")
            
        except Exception as e:
            error_count += 1
            print(f"✗ Error processing {file_path.name}: {e}")
    
    print(f"\n{'='*60}")
    print(f"Organization complete!")
    print(f"Copied: {copied_count} files")
    print(f"Skipped: {skipped_count} files (older than cutoff)")
    print(f"Errors: {error_count} files")
    print(f"Location: {base_output}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    import sys
    
    source_dir = "/Users/KevinHG/Documents/Copy to HG Main (weekly cron job)/AI Chat Exports "
    vault_path = "/Users/KevinHG/Documents/HG Main"
    days_back = 7  # Test mode
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "all":
            days_back = 0
        else:
            days_back = int(sys.argv[1])
    
    organize_chat_exports(source_dir, vault_path, days_back)

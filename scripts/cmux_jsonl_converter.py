#!/usr/bin/env python3
"""
Convert CMUX JSONL chat files to readable Markdown
"""

import json
import re
from pathlib import Path
from datetime import datetime

def sanitize_filename(text):
    """Create safe filename from text"""
    # Remove special characters
    text = re.sub(r'[<>:"/\\|?*]', '', text)
    text = re.sub(r'[\n\r]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text[:100].strip()

def extract_title_from_messages(messages):
    """Extract a reasonable title from first user message"""
    for msg in messages:
        if msg.get('role') == 'user':
            parts = msg.get('parts', [])
            for part in parts:
                if part.get('type') == 'text':
                    text = part.get('text', '').strip()
                    if text:
                        # Get first sentence or first 60 chars
                        first_line = text.split('\n')[0]
                        if len(first_line) > 60:
                            first_line = first_line[:60] + "..."
                        return first_line
    return "Untitled Conversation"

def parse_timestamp(ts):
    """Parse timestamp from milliseconds to datetime"""
    if ts:
        try:
            return datetime.fromtimestamp(ts / 1000)
        except:
            pass
    return datetime.now()

def convert_message_to_markdown(msg):
    """Convert a single message to markdown format"""
    role = msg.get('role', 'unknown')
    metadata = msg.get('metadata', {})
    timestamp = parse_timestamp(metadata.get('timestamp'))
    
    # Role header
    if role == 'user':
        header = f"## 👤 User"
    elif role == 'assistant':
        header = f"## 🤖 Assistant"
    else:
        header = f"## {role.title()}"
    
    # Add timestamp
    header += f" *({timestamp.strftime('%Y-%m-%d %H:%M:%S')})*"
    
    # Extract content
    parts = msg.get('parts', [])
    content_blocks = []
    
    for part in parts:
        if part.get('type') == 'text':
            content_blocks.append(part.get('text', ''))
        elif part.get('type') == 'tool_call':
            tool_name = part.get('name', 'unknown')
            content_blocks.append(f"```\n🔧 Tool Call: {tool_name}\n```")
        elif part.get('type') == 'tool_result':
            content_blocks.append(f"```\n📊 Tool Result\n```")
    
    content = '\n\n'.join(content_blocks)
    
    return f"{header}\n\n{content}\n\n---\n"

def convert_jsonl_to_markdown(jsonl_path, output_path, session_id):
    """Convert JSONL chat file to markdown"""
    messages = []
    first_timestamp = None
    last_timestamp = None
    
    # Read JSONL file
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                msg = json.loads(line)
                messages.append(msg)
                
                # Track timestamps
                ts = msg.get('metadata', {}).get('timestamp')
                if ts:
                    if not first_timestamp or ts < first_timestamp:
                        first_timestamp = ts
                    if not last_timestamp or ts > last_timestamp:
                        last_timestamp = ts
            except json.JSONDecodeError as e:
                print(f"Warning: Could not parse line in {jsonl_path}: {e}")
                continue
    
    if not messages:
        print(f"Warning: No messages found in {jsonl_path}")
        return None
    
    # Extract title and date
    title = extract_title_from_messages(messages)
    chat_date = parse_timestamp(first_timestamp) if first_timestamp else datetime.now()
    
    # Create YAML frontmatter
    yaml = f"""---
source: CMUX
date: {chat_date.strftime('%Y-%m-%d')}
chat_id: {session_id}
title: "{title}"
message_count: {len(messages)}
---

# {title}

**Session ID:** `{session_id}`  
**Date:** {chat_date.strftime('%B %d, %Y')}  
**Messages:** {len(messages)}

---

"""
    
    # Convert messages
    markdown_messages = [convert_message_to_markdown(msg) for msg in messages]
    
    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(yaml)
        f.write('\n'.join(markdown_messages))
    
    return {
        'title': title,
        'date': chat_date,
        'message_count': len(messages)
    }

def convert_all_cmux_chats(source_dir, vault_path):
    """Convert all CMUX backup chat files"""
    source_dir = Path(source_dir)
    vault_path = Path(vault_path)
    
    print("Converting CMUX JSONL files to Markdown...")
    print(f"Source: {source_dir}")
    print(f"Target: {vault_path / 'AI Chats'}")
    print()
    
    # Find all chat.jsonl files
    jsonl_files = list(source_dir.glob("*/chat.jsonl"))
    
    if not jsonl_files:
        print("No chat.jsonl files found!")
        return
    
    print(f"Found {len(jsonl_files)} chat files\n")
    
    converted = []
    
    for jsonl_file in jsonl_files:
        session_id = jsonl_file.parent.name
        
        try:
            # Parse to get date first
            with open(jsonl_file, 'r') as f:
                first_line = f.readline()
                if first_line:
                    msg = json.loads(first_line)
                    ts = msg.get('metadata', {}).get('timestamp')
                    chat_date = parse_timestamp(ts) if ts else datetime.now()
                else:
                    chat_date = datetime.now()
            
            # Determine output path (monthly for CMUX)
            year = chat_date.year
            month = chat_date.strftime('%b')  # Nov, Dec, etc.
            output_dir = vault_path / "AI Chats" / str(year) / month
            
            # Get title for filename
            temp_info = convert_jsonl_to_markdown(
                jsonl_file,
                output_dir / "temp.md",  # Temp path
                session_id
            )
            
            if temp_info:
                # Create proper filename
                safe_title = sanitize_filename(temp_info['title'])
                date_str = temp_info['date'].strftime('%Y-%m-%d')
                filename = f"CMUX - {safe_title} {date_str}.md"
                final_path = output_dir / filename
                
                # Rename temp file
                (output_dir / "temp.md").rename(final_path)
                
                print(f"✓ {filename}")
                converted.append(temp_info)
            
        except Exception as e:
            print(f"✗ Error converting {session_id}: {e}")
    
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"Converted: {len(converted)} chats")
    print(f"Location: {vault_path / 'AI Chats'}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    import sys
    
    source_dir = "/Users/KevinHG/Documents/Copy to HG Main (weekly cron job)/CMUX backups"
    vault_path = "/Users/KevinHG/Documents/HG Main"
    
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    if len(sys.argv) > 2:
        vault_path = sys.argv[2]
    
    convert_all_cmux_chats(source_dir, vault_path)

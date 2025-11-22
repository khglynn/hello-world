#!/usr/bin/env python3
"""
Organize screenshots into Obsidian vault by quarter
Optionally compress images
"""

import os
import shutil
import subprocess
from pathlib import Path
from datetime import datetime, timedelta

def get_quarter(date):
    """Get quarter (Q1-Q4) from date"""
    month = date.month
    return f"Q{(month - 1) // 3 + 1}"

def get_image_date(file_path):
    """Get date from image file (modification time)"""
    mtime = os.path.getmtime(file_path)
    return datetime.fromtimestamp(mtime)

def compress_image(source_path, output_path):
    """
    Compress image using built-in tools (sips on macOS)
    Returns True if compression succeeded
    """
    try:
        # Use sips (built-in macOS tool) for compression
        # Reduce quality to 75% for JPG/PNG
        subprocess.run(
            ['sips', '--setProperty', 'formatOptions', '75', source_path, '--out', output_path],
            capture_output=True,
            check=True,
            timeout=30
        )
        return True
    except:
        # If compression fails, just copy
        shutil.copy2(source_path, output_path)
        return False

def organize_screenshots(source_dir, vault_path, days_back=7, compress=False):
    """
    Organize screenshots into vault by quarter
    
    Args:
        source_dir: Source directory with screenshots
        vault_path: Target Obsidian vault
        days_back: Only copy files from last N days (0 = all)
        compress: If True, compress images before copying
    """
    source_dir = Path(source_dir)
    vault_path = Path(vault_path)
    base_output = vault_path / "Screenshots"
    
    # Calculate cutoff date
    if days_back > 0:
        cutoff_date = datetime.now() - timedelta(days=days_back)
    else:
        cutoff_date = datetime(2000, 1, 1)
    
    print(f"Organizing Screenshots...")
    print(f"Source: {source_dir}")
    print(f"Target: {base_output}")
    print(f"Filter: Files from last {days_back} days (after {cutoff_date.strftime('%Y-%m-%d')})")
    print(f"Compression: {'Enabled' if compress else 'Disabled'}")
    print()
    
    # Find all image files
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.heic'}
    image_files = [f for f in source_dir.iterdir() 
                   if f.is_file() and f.suffix.lower() in image_extensions]
    
    print(f"Found {len(image_files)} image files")
    print("Processing...\n")
    
    copied_count = 0
    skipped_count = 0
    compressed_count = 0
    error_count = 0
    
    for file_path in image_files:
        try:
            # Get file date
            file_date = get_image_date(file_path)
            
            # Skip if older than cutoff
            if file_date < cutoff_date:
                skipped_count += 1
                continue
            
            # Determine output folder (quarterly)
            year = file_date.year
            quarter = get_quarter(file_date)
            output_dir = base_output / str(year) / quarter
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Create output path
            output_path = output_dir / file_path.name
            
            # Handle duplicates
            counter = 1
            while output_path.exists():
                stem = file_path.stem
                suffix = file_path.suffix
                output_path = output_dir / f"{stem} ({counter}){suffix}"
                counter += 1
            
            # Copy (with optional compression)
            if compress:
                if compress_image(file_path, output_path):
                    compressed_count += 1
            else:
                shutil.copy2(file_path, output_path)
            
            copied_count += 1
            if copied_count % 50 == 0:
                print(f"  Progress: {copied_count} files copied...")
            
        except Exception as e:
            error_count += 1
            print(f"✗ Error processing {file_path.name}: {e}")
    
    print(f"\n{'='*60}")
    print(f"Organization complete!")
    print(f"Copied: {copied_count} files")
    if compress:
        print(f"Compressed: {compressed_count} files")
    print(f"Skipped: {skipped_count} files (older than cutoff)")
    print(f"Errors: {error_count} files")
    print(f"Location: {base_output}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    import sys
    
    source_dir = "/Users/KevinHG/Desktop/Screenshots"
    vault_path = "/Users/KevinHG/Documents/HG Main"
    days_back = 7  # Test mode
    compress = False
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "all":
            days_back = 0
        else:
            days_back = int(sys.argv[1])
    
    if len(sys.argv) > 2 and sys.argv[2] == "--compress":
        compress = True
    
    organize_screenshots(source_dir, vault_path, days_back, compress)

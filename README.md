# Obsidian Automation Suite

A complete automation system for Obsidian knowledge management, featuring:
- Automated organization of screenshots, AI chats, and notes
- CMUX conversation converter (JSONL → Markdown)
- Cross-device sync via Remotely Save + WebDAV
- Weekly cron job automation
- Zero-cost local AI search with Smart Connections

## Features

- **Automated Organization**: Screenshots by quarter, AI chats by month
- **Rich Metadata**: YAML frontmatter with dates, sources, URLs, message counts
- **Cross-Platform**: Mac, iPhone, iPad support
- **Privacy-First**: Local embeddings, your data stays on your hardware
- **Zero Cost**: No monthly fees, runs entirely on your equipment

## Quick Start

```bash
cd scripts
cat START_HERE.md
```

## Documentation

- **[START_HERE.md](scripts/START_HERE.md)** - Getting started guide
- **[README.md](scripts/README.md)** - Complete documentation
- **[REMOTELY_SAVE_SETUP.md](scripts/REMOTELY_SAVE_SETUP.md)** - Cloud sync guide
- **[QUICK_REFERENCE.md](scripts/QUICK_REFERENCE.md)** - Command cheat sheet

## Scripts

### Organization
- `organize_screenshots.py` - Organize by quarter (2025/Q4/)
- `organize_ai_chats.py` - Organize by month (2025/Nov/)
- `cmux_jsonl_converter.py` - Convert CMUX JSONL to markdown

### Automation
- `weekly_obsidian_sync.sh` - Main automation orchestrator
- `install_cron_jobs.sh` - Setup weekly cron jobs
- `uninstall_cron_jobs.sh` - Remove automation

### Utilities
- `copy_obsidian_settings.sh` - Copy plugins/settings between vaults

## Use Cases

- **Knowledge Workers**: Organize thousands of AI conversations
- **Researchers**: Searchable archive of all interactions
- **Note-Takers**: Automated screenshot management
- **Multi-Device Users**: Free sync across Mac/iPhone/iPad

## Requirements

- macOS (for cron jobs)
- Python 3.6+
- Obsidian
- Optional: Synology NAS for WebDAV sync

## Cost

**$0/month** - Everything runs locally. Optional Synology NAS for sync (one-time hardware cost).

Compare to:
- Obsidian Sync: $4-8/month
- Dropbox: $12/month
- Notion: $10/month

## License

MIT - Use freely for personal or commercial projects

## Author

Built for personal knowledge management automation.

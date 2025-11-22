# 📚 Documentation Index

Quick navigation for all documentation files.

---

## 🎯 Start Here (First Time Users)

**→ [START_HERE.md](START_HERE.md)** - Read this first!  
Your complete onboarding guide with next steps.

---

## 📖 Documentation Files

### Quick Reference
**→ [QUICK_REFERENCE.md](QUICK_REFERENCE.md)**  
Cheat sheet with common commands and workflows.  
*Read time: 2 minutes*

### Complete Guide  
**→ [README.md](README.md)**  
Full documentation covering all features and troubleshooting.  
*Read time: 15 minutes*

### Cloud Sync Setup
**→ [REMOTELY_SAVE_SETUP.md](REMOTELY_SAVE_SETUP.md)**  
Step-by-step guide to setup free WebDAV sync with Synology.  
*Read time: 10 minutes*

---

## 🛠 Scripts & Tools

### Automation Scripts
- `weekly_obsidian_sync.sh` - Main sync script (called by cron)
- `install_cron_jobs.sh` - Install weekly automation
- `uninstall_cron_jobs.sh` - Remove automation

### Organization Scripts  
- `organize_screenshots.py` - Organize by quarter
- `organize_ai_chats.py` - Organize by month
- `cmux_jsonl_converter.py` - Convert CMUX to markdown

### Utility Scripts
- `copy_obsidian_settings.sh` - Copy plugins between vaults

---

## 📍 Quick Links

**View sync log:**
```bash
tail -50 ~/.obsidian_sync_log.txt
```

**Run sync manually:**
```bash
cd ~/.cmux/src/hello-world/qna/scripts
./weekly_obsidian_sync.sh
```

**Import everything:**
```bash
python3 organize_ai_chats.py all
python3 organize_screenshots.py all
```

---

## 🆘 Troubleshooting

1. Check sync log: `tail -50 ~/.obsidian_sync_log.txt`
2. See troubleshooting section in README.md
3. Run manual test: `./weekly_obsidian_sync.sh`

---

## 📊 Files Created

| File | Size | Purpose |
|------|------|---------|
| START_HERE.md | 8.9KB | Getting started guide |
| README.md | 11KB | Complete documentation |
| REMOTELY_SAVE_SETUP.md | 9.3KB | Cloud sync guide |
| QUICK_REFERENCE.md | 3.5KB | Command cheat sheet |
| INDEX.md | 1.5KB | This file |

**Total documentation:** ~34KB of comprehensive guides

---

**Ready to begin?** → [START_HERE.md](START_HERE.md)

# Obsidian Automation Scripts

Complete automation for your Obsidian vault sync, organization, and backup.

## 📁 What's Included

### Core Scripts
- **`weekly_obsidian_sync.sh`** - Main sync script (called by cron)
- **`organize_screenshots.py`** - Organizes screenshots by quarter
- **`organize_ai_chats.py`** - Organizes AI chat exports by month
- **`cmux_jsonl_converter.py`** - Converts CMUX chats to markdown
- **`copy_obsidian_settings.sh`** - Copy plugins/settings between vaults

### Management Scripts
- **`install_cron_jobs.sh`** - Install weekly automation
- **`uninstall_cron_jobs.sh`** - Remove automation
- **`REMOTELY_SAVE_SETUP.md`** - Complete WebDAV sync guide

---

## 🚀 Quick Start (First Time Setup)

### 1. Install Weekly Automation

```bash
cd ~/.cmux/src/hello-world/qna/scripts
./install_cron_jobs.sh
```

**This installs a weekly cron job (Sundays at 9 AM) that:**
- ✅ Syncs last 7 days of screenshots → Obsidian
- ✅ Syncs last 7 days of AI chat exports → Obsidian
- ✅ Converts new CMUX conversations → markdown
- ✅ Copies anything from `~/Desktop/Copy to Obsidian/` → vault
- ✅ Syncs staging folder → vault

### 2. Setup Cloud Sync (Optional but Recommended)

```bash
cat REMOTELY_SAVE_SETUP.md
```

Follow the guide to setup free, unlimited sync using your Synology NAS.

---

## 📋 Daily Usage

### Adding Content to Obsidian

**Screenshots:**
- Save to: `~/Desktop/Screenshots/`
- Auto-syncs: Every Sunday
- Goes to: `HG Main/Screenshots/YYYY/QX/`

**Quick Notes/Files:**
- Save to: `~/Desktop/Copy to Obsidian/`
- Auto-syncs: Every Sunday
- Goes to: `HG Main/` (preserves folder structure)

**AI Chats:**
- Export to: `~/Documents/Copy to HG Main (weekly cron job)/AI Chat Exports /`
- Auto-syncs: Every Sunday
- Goes to: `HG Main/AI Chats/YYYY/MMM/`

**CMUX Conversations:**
- Save session to: `~/Documents/Copy to HG Main (weekly cron job)/CMUX backups/`
- Auto-converts: Every Sunday
- Goes to: `HG Main/AI Chats/YYYY/MMM/`

### Manual Sync (Don't Wait for Sunday)

```bash
cd ~/.cmux/src/hello-world/qna/scripts
./weekly_obsidian_sync.sh
```

---

## 🛠 Manual Operations

### Run Individual Scripts

**Organize screenshots from last 7 days:**
```bash
python3 organize_screenshots.py 7
```

**Organize screenshots from last 30 days:**
```bash
python3 organize_screenshots.py 30
```

**Organize ALL screenshots:**
```bash
python3 organize_screenshots.py all
```

**With compression:**
```bash
python3 organize_screenshots.py 7 --compress
```

---

**Organize AI chats from last 7 days:**
```bash
python3 organize_ai_chats.py 7
```

**Organize ALL AI chats:**
```bash
python3 organize_ai_chats.py all
```

---

**Convert CMUX chats:**
```bash
python3 cmux_jsonl_converter.py
```

---

**Copy settings between vaults:**
```bash
./copy_obsidian_settings.sh "/path/to/source/vault" "/path/to/target/vault"
```

---

### View Sync Logs

**See what the cron job is doing:**
```bash
tail -50 ~/.obsidian_sync_log.txt
```

**Watch log in real-time:**
```bash
tail -f ~/.obsidian_sync_log.txt
```

**View all logs:**
```bash
cat ~/.obsidian_sync_log.txt
```

---

### Manage Cron Jobs

**View installed cron jobs:**
```bash
crontab -l
```

**Uninstall automation:**
```bash
./uninstall_cron_jobs.sh
```

**Reinstall automation:**
```bash
./install_cron_jobs.sh
```

---

## 🖥 Setup on Second Mac

### Copy Scripts to Second Mac

**Option 1: Using scp (if Macs are networked):**
```bash
scp -r ~/.cmux/src/hello-world/qna/scripts username@second-mac:~/obsidian-scripts/
```

**Option 2: Manual copy:**
1. Copy folder: `~/.cmux/src/hello-world/qna/scripts/`
2. To second Mac: `~/obsidian-scripts/`
3. Via USB drive, AirDrop, or network share

### Install on Second Mac

```bash
# On second Mac
cd ~/obsidian-scripts
chmod +x *.sh
./install_cron_jobs.sh
```

Now both Macs will independently sync to the Obsidian vault, and Remotely Save will keep them synchronized via Synology.

---

## 📱 iPhone Setup

**No scripts needed!** Just setup Remotely Save plugin:

1. Open Obsidian mobile app
2. Settings → Community Plugins → Remotely Save
3. Use same WebDAV settings as desktop
4. Sync Now

See `REMOTELY_SAVE_SETUP.md` for detailed mobile setup.

---

## 🗂 Folder Structure

After automation, your Obsidian vault will look like:

```
HG Main/
├── AI Chats/
│   ├── 2025/
│   │   ├── Oct/
│   │   │   ├── CMUX - Obsidian Setup 2025-10-29.md
│   │   │   ├── ChatGPT - Python Script 2025-10-25.md
│   │   │   └── Claude - Resume Help 2025-10-28.md
│   │   └── Nov/
│   │       ├── CMUX - Recent Chat 2025-11-21.md
│   │       └── Gemini - Job Search 2025-11-20.md
│   └── 2024/
│       └── [Older chats...]
│
├── Screenshots/
│   ├── 2025/
│   │   ├── Q1/ (Jan-Mar)
│   │   ├── Q2/ (Apr-Jun)
│   │   ├── Q3/ (Jul-Sep)
│   │   └── Q4/ (Oct-Dec)
│   │       ├── Screenshot 2025-11-21.png
│   │       └── Screenshot 2025-11-20.png
│   └── 2024/
│
├── Apple Notes/ (manual export)
│   ├── 2025/
│   │   ├── Q1/
│   │   ├── Q2/
│   │   ├── Q3/
│   │   └── Q4/
│   │       ├── Meeting Notes 2025-11-21.md
│   │       └── Meeting Notes 2025-11-21/
│   │           ├── photo.png
│   │           └── document.pdf
│   └── Archive/
│       ├── 2024/
│       └── 2023/
│
├── Daily Notes/
│   ├── 2025-11-21.md
│   └── 2025-11-20.md
│
└── [Other notes and folders...]
```

---

## 🔍 Search & Organization

### Finding Content

**Smart Connections (AI-powered):**
- Open any note
- Related notes appear in sidebar automatically
- Search bar: semantic search (understands meaning)
- Example: "resume writing" finds related chats even without exact words

**Omnisearch (Keyword):**
- Cmd+P → Search
- Searches note content + OCR'd screenshots
- Fast, exact keyword matching

**Native Obsidian Search:**
- Cmd+Shift+F
- Searches all notes (except excluded folders)

### Excluded from Search

These folders are **excluded from native Obsidian search** but indexed by Smart Connections:

- `Apple Notes/Archive/` - Old apple notes (pre-2025)

**To add more exclusions:**
1. Settings → Files & Links → Excluded files
2. Add pattern: `folder-name/**`

**To exclude from Smart Connections too:**
1. Settings → Smart Connections → Folder Exclusions
2. Add: `Apple Notes/Archive`

---

## ⚙️ Customization

### Change Sync Schedule

Edit the cron job:

```bash
crontab -e
```

**Current schedule (Sunday 9 AM):**
```
0 9 * * 0 /path/to/weekly_obsidian_sync.sh
```

**Daily at 9 AM:**
```
0 9 * * * /path/to/weekly_obsidian_sync.sh
```

**Every 6 hours:**
```
0 */6 * * * /path/to/weekly_obsidian_sync.sh
```

**Twice a week (Wed & Sun at 9 AM):**
```
0 9 * * 0,3 /path/to/weekly_obsidian_sync.sh
```

Save and exit (`:wq` in vim)

### Change Days to Sync

Edit `weekly_obsidian_sync.sh`:

**Line 14 - Screenshots sync window:**
```bash
python3 "$SCRIPT_DIR/organize_screenshots.py" 30  # Change 7 to 30 for last 30 days
```

**Line 18 - AI chats sync window:**
```bash
python3 "$SCRIPT_DIR/organize_ai_chats.py" 30  # Change 7 to 30
```

### Add More Sync Sources

Edit `weekly_obsidian_sync.sh`, add before the final log line:

```bash
# Sync Documents folder
DOCS_FOLDER="/Users/KevinHG/Documents/Important Docs"
if [ -d "$DOCS_FOLDER" ]; then
    echo "Syncing documents..." >> "$LOG_FILE"
    rsync -av --update "$DOCS_FOLDER/" "$VAULT_PATH/Documents/" >> "$LOG_FILE" 2>&1
fi
```

---

## 🐛 Troubleshooting

### Cron job not running

**Check if job is installed:**
```bash
crontab -l
```

**Check log for errors:**
```bash
cat ~/.obsidian_sync_log.txt
```

**Test manually:**
```bash
./weekly_obsidian_sync.sh
```

**Common issues:**
- Script paths are absolute (no `~/` shortcuts in cron)
- Python3 must be in PATH
- File permissions (scripts must be executable: `chmod +x`)

### Scripts fail with "Permission denied"

```bash
chmod +x ~/.cmux/src/hello-world/qna/scripts/*.sh
```

### Python errors

**Check Python3 is available:**
```bash
which python3
python3 --version
```

**Most scripts require Python 3.6+**

### Files not appearing in Obsidian

1. **Check sync log:**
   ```bash
   tail -50 ~/.obsidian_sync_log.txt
   ```

2. **Verify source folders exist:**
   - `~/Desktop/Screenshots/`
   - `~/Desktop/Copy to Obsidian/`
   - `~/Documents/Copy to HG Main (weekly cron job)/`

3. **Check target vault path:**
   - Default: `/Users/KevinHG/Documents/HG Main/`
   - Edit in scripts if your vault is elsewhere

4. **Manual sync test:**
   ```bash
   ./weekly_obsidian_sync.sh
   cat ~/.obsidian_sync_log.txt
   ```

---

## 📚 Additional Resources

**Obsidian Plugin Docs:**
- [Smart Connections](https://github.com/brianpetro/obsidian-smart-connections)
- [Remotely Save](https://github.com/remotely-save/remotely-save)
- [Omnisearch](https://github.com/scambier/obsidian-omnisearch)
- [Tasks Plugin](https://github.com/obsidian-tasks-group/obsidian-tasks)

**Synology WebDAV:**
- [Official WebDAV Guide](https://kb.synology.com/en-global/DSM/help/DSM/AdminCenter/file_webdav)
- [Tailscale Setup](https://tailscale.com/kb/1131/synology/)

**Cron Job Help:**
- [Crontab Guru](https://crontab.guru/) - Cron schedule expression editor
- [Mac Cron Guide](https://www.taniarascia.com/setting-up-a-basic-cron-job-in-mac-osx/)

---

## 📝 Notes

### Test Batch Complete

**You've imported (last 7 days only):**
- ✅ 6 CMUX conversations (all sessions)
- ✅ 6 AI chat exports (recent)
- ✅ 8 screenshots
- ✅ 34 plugins + settings copied

**To import everything:**
```bash
# Import ALL AI chats (2,443 files)
python3 organize_ai_chats.py all

# Import ALL screenshots (755 files)
python3 organize_screenshots.py all
```

### Apple Notes Export

Apple Notes automation requires Full Disk Access for Terminal (macOS security).

**For now, manual export:**
1. Open Apple Notes
2. Select notes to export
3. File → Export as PDF (or print to PDF)
4. Save to: `~/Desktop/Copy to Obsidian/Apple Notes/`
5. Sunday cron will sync them

**OR** Grant Terminal Full Disk Access:
1. System Preferences → Security & Privacy → Privacy
2. Full Disk Access → Add Terminal
3. Restart Terminal
4. Run: `python3 apple_notes_exporter.py`

---

## 🎉 You're All Set!

Your Obsidian vault now has:
- ✅ Automated weekly syncing
- ✅ AI chat organization
- ✅ Screenshot management
- ✅ Cross-device sync (via Remotely Save)
- ✅ All plugins and settings configured
- ✅ Smart search and organization

**Next steps:**
1. Follow `REMOTELY_SAVE_SETUP.md` to enable sync
2. Let it run for a week
3. Check `~/.obsidian_sync_log.txt` to verify
4. Adjust sync frequency if needed

**Questions or issues?** Check the logs first, then review the troubleshooting section.

Enjoy your fully automated knowledge management system! 🚀

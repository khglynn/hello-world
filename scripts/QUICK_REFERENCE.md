# Quick Reference - Obsidian Automation

## 🚨 Most Common Commands

```bash
# Navigate to scripts
cd ~/.cmux/src/hello-world/qna/scripts

# Run sync now (don't wait for Sunday)
./weekly_obsidian_sync.sh

# View what last sync did
tail -50 ~/.obsidian_sync_log.txt

# Check if automation is installed
crontab -l

# Import all remaining AI chats
python3 organize_ai_chats.py all

# Import all remaining screenshots
python3 organize_screenshots.py all
```

---

## 📂 Drop Folders (Auto-Syncs Weekly)

| Put files here... | They go here... |
|---|---|
| `~/Desktop/Screenshots/` | `HG Main/Screenshots/YYYY/QX/` |
| `~/Desktop/Copy to Obsidian/` | `HG Main/` (root) |
| `~/Documents/Copy to HG Main (weekly cron job)/AI Chat Exports /` | `HG Main/AI Chats/YYYY/MMM/` |
| `~/Documents/Copy to HG Main (weekly cron job)/CMUX backups/` | `HG Main/AI Chats/YYYY/MMM/` |

---

## ⏰ Automation Schedule

**Current:** Every Sunday at 9:00 AM

**To change:**
```bash
crontab -e
# Edit the time in format: minute hour day month weekday
# Current: 0 9 * * 0
# Save and exit (:wq)
```

**Common schedules:**
- Daily 9 AM: `0 9 * * *`
- Every 6 hours: `0 */6 * * *`
- Mon/Wed/Fri 9 AM: `0 9 * * 1,3,5`

---

## 🔧 Management Commands

```bash
# Install automation
./install_cron_jobs.sh

# Remove automation
./uninstall_cron_jobs.sh

# Copy settings between vaults
./copy_obsidian_settings.sh "/source/vault" "/target/vault"
```

---

## 📱 Remotely Save (Cloud Sync)

**Plugin already installed** - just needs WebDAV config.

**See full guide:**
```bash
cat REMOTELY_SAVE_SETUP.md
```

**Quick config:**
1. Obsidian Settings → Remotely Save
2. Service: WebDAV
3. Server: `https://[synology-ip]:5006`
4. Path: `/Obsidian/HG Main/`
5. Test connection → Sync Now

---

## 🔍 Smart Connections (Zero Cost AI Search)

**Your settings:**
- Embeddings: Local (Transformers.js)
- Model: `TaylorAI/bge-micro-v2`
- **No API costs, no tokens used!**

**Usage:**
- Open any note → Related notes appear in sidebar
- Search bar: Understands meaning, not just keywords
- Example: "resume tips" finds related chats

**If search is slow/bad:**
1. Settings → Smart Connections
2. Click "Create New Base" (rebuilds index)
3. Wait 10-15 minutes for 2,443 chats

---

## 📊 What's Been Imported (Test Batch)

| Type | Count | Location |
|------|-------|----------|
| CMUX chats | 6 | AI Chats/2025/ |
| AI exports | 6 | AI Chats/2025/ |
| Screenshots | 8 | Screenshots/2025/Q4/ |
| Plugins | 34 | .obsidian/plugins/ |

**Still to import:**
- 2,437 AI chat exports (run: `python3 organize_ai_chats.py all`)
- 747 screenshots (run: `python3 organize_screenshots.py all`)
- 280 Apple Notes (manual export needed)

---

## ❗️ Troubleshooting One-Liners

```bash
# Cron not working?
crontab -l  # Should show one line with weekly_obsidian_sync.sh

# Scripts won't run?
chmod +x ~/.cmux/src/hello-world/qna/scripts/*.sh

# Want to see sync happening live?
tail -f ~/.obsidian_sync_log.txt

# Remotely Save failing?
# Obsidian Settings → Remotely Save → View Logs

# Second Mac not syncing?
# 1. Copy scripts folder to second Mac
# 2. cd ~/obsidian-scripts && ./install_cron_jobs.sh
```

---

## 🎯 Next Steps

1. **Setup cloud sync** (20 min):
   ```bash
   cat REMOTELY_SAVE_SETUP.md
   ```

2. **Import remaining chats** (5 min):
   ```bash
   python3 organize_ai_chats.py all
   ```

3. **Test automation** (2 min):
   ```bash
   ./weekly_obsidian_sync.sh
   tail -50 ~/.obsidian_sync_log.txt
   ```

4. **Setup second Mac/iPhone** (15 min):
   - See README.md sections

---

**Full docs:** `cat README.md`

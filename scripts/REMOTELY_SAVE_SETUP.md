# Remotely Save + Synology WebDAV Setup Guide

This guide will help you set up free, unlimited sync for your Obsidian vault using:
- **Remotely Save plugin** (already installed in your vault)
- **Synology NAS WebDAV** (you own the hardware, no recurring costs)

---

## Part 1: Enable WebDAV on Synology NAS

### Step 1: Enable WebDAV Service

1. **Open Synology DSM** (Disk Station Manager)
   - In your browser, go to your Synology's IP address
   - Or use QuickConnect if configured

2. **Open Control Panel** → **File Services**

3. **Go to WebDAV tab** (or rsync/WebDAV tab on newer DSM)

4. **Enable WebDAV:**
   - ☑ Enable WebDAV
   - HTTP port: `5005` (default)
   - ☑ Enable HTTPS
   - HTTPS port: `5006` (default)
   - **Use HTTPS for security!**

5. **Click Apply**

### Step 2: Create Obsidian Sync Folder

1. **Open File Station** on your Synology

2. **Navigate to your home directory** or create a shared folder:
   - Recommended location: `/homes/[your-username]/Obsidian/`
   - Or: Create a new shared folder called `Obsidian`

3. **Create folder structure:**
   ```
   Obsidian/
   └── HG Main/
   ```

4. **Set permissions:**
   - Right-click folder → Properties → Permissions
   - Ensure your user has Read/Write access

---

## Part 2: Configure Remotely Save in Obsidian

### Step 1: Open Plugin Settings

1. **Open Obsidian**
2. **Settings** (⚙️) → **Community Plugins** → **Remotely Save**

### Step 2: Configure WebDAV Connection

**Choose Remote Service:**
- Select: `WebDAV`

**Server Address:**
```
https://[YOUR-SYNOLOGY-IP]:5006
```
Example: `https://192.168.1.100:5006`

**Username:**
- Your Synology username (same as DSM login)

**Password:**
- Your Synology password
- **Note:** Password is encrypted and stored locally

**Base Path:**
```
/Obsidian/HG Main/
```
- This is the folder path on your Synology
- Include leading and trailing slashes

**Auth Type:**
- Select: `Basic Auth` (default)

**Depth:**
- Leave as: `auto` or `manual_1`

### Step 3: Test Connection

1. **Click "Check" button** next to server address
2. You should see: ✅ "Connection successful"

**If you see an error:**
- ❌ "Cannot connect": Check IP address and port
- ❌ "Authentication failed": Check username/password
- ❌ "SSL error": Try HTTP port 5005 temporarily (not recommended)
- ❌ "Path not found": Create the folder `/Obsidian/HG Main/` on Synology

### Step 4: Configure Sync Settings

**Auto Sync:**
- Enable: `☑ Auto sync every X minutes`
- Interval: `10` minutes (or your preference)
- ☑ Auto sync on startup

**Sync Strategy:**
- **Recommended:** `Last modified time wins`
- This prevents conflicts and syncs newest version

**Files to Skip:**
- Add patterns for files you DON'T want to sync:
  ```
  .obsidian/workspace.json
  .obsidian/workspace-mobile.json
  .trash/
  .DS_Store
  ```

**Folders to Exclude:**
- Apple Notes/Archive/
- .obsidian/plugins/*/node_modules/

### Step 5: Initial Sync

1. **Click "Sync Now" button**
2. **Watch the sync status** in bottom-right corner
3. **First sync will take 5-10 minutes** (uploads your entire vault)

**Progress indicators:**
- 🔄 "Syncing..." = In progress
- ✅ "Synced" = Complete
- ❌ "Sync failed" = Check connection

---

## Part 3: Enable Remote Access (Optional)

If you want to sync when away from home, you need remote access to your Synology.

### Option A: Synology QuickConnect (Easiest - 5 minutes)

1. **DSM Control Panel** → **QuickConnect**
2. **Enable QuickConnect**
3. **Register ID:** Choose a unique ID (e.g., `kevinhg-nas`)
4. **Done!**

**Update Obsidian settings:**
- Server Address: `https://[your-quickconnect-id].quickconnect.to:5006`
- Example: `https://kevinhg-nas.quickconnect.to:5006`

**Pros:** Easy, no port forwarding
**Cons:** Slower than direct connection (routes through Synology servers)

### Option B: Tailscale VPN (Recommended - 15 minutes)

Tailscale creates a secure private network across your devices.

1. **Install Tailscale on Synology:**
   - Package Center → Search "Tailscale" → Install
   - Open Tailscale → Login with your account
   
2. **Install Tailscale on Mac:**
   - Download from https://tailscale.com/download
   - Install and login with same account

3. **Install Tailscale on iPhone:**
   - App Store → "Tailscale" → Install
   - Login with same account

4. **Get Synology Tailscale IP:**
   - Open Tailscale on Synology
   - Copy the IP (looks like `100.x.x.x`)

**Update Obsidian settings:**
- Server Address: `https://100.x.x.x:5006`
- (Use your Tailscale IP)

**Pros:** Fast, secure, direct connection
**Cons:** Requires Tailscale app running on devices

---

## Part 4: Setup on iPhone/iPad

1. **Open Obsidian mobile app**
2. **Open your vault**
3. **Settings** → **Community Plugins** → **Remotely Save**
4. **Use the SAME settings as desktop:**
   - Server: Your Synology address (or QuickConnect/Tailscale)
   - Username, password, base path (all same)
5. **Sync Now**

**First mobile sync:**
- Downloads entire vault to iPhone
- May take 10-15 minutes on first run
- Subsequent syncs are fast (only changed files)

---

## Part 5: Setup on Second MacBook

1. **Copy the scripts folder** to your second Mac:
   ```bash
   scp -r ~/.cmux/src/hello-world/qna/scripts [SECOND-MAC]:~/obsidian-scripts/
   ```

2. **Or manually:**
   - Copy folder: `/Users/KevinHG/.cmux/src/hello-world/qna/scripts`
   - To second Mac at: `~/obsidian-scripts/`

3. **Install cron job on second Mac:**
   ```bash
   cd ~/obsidian-scripts
   ./install_cron_jobs.sh
   ```

4. **Answer the prompts**

**Sync flow with two Macs:**
- Mac 1: Creates screenshots/notes → Cron copies to Obsidian → Remotely Save uploads to Synology
- Synology: Central sync hub
- Mac 2: Remotely Save downloads from Synology
- iPhone: Remotely Save syncs both ways

---

## Troubleshooting

### "Connection refused" error
- ✅ Check Synology IP address is correct
- ✅ Verify WebDAV is enabled in File Services
- ✅ Try HTTP port 5005 (temporarily)
- ✅ Check firewall settings on Synology

### "SSL certificate error"
- Option 1: Install proper SSL cert on Synology (Control Panel → Security → Certificate)
- Option 2: Use HTTP temporarily (not secure)
- Option 3: Add exception in Obsidian

### Sync is slow
- ✅ Exclude large folders (Apple Notes/Archive)
- ✅ Check network speed
- ✅ Reduce sync frequency
- ✅ Use Tailscale instead of QuickConnect

### Files not syncing
- ✅ Check "Files to Skip" settings
- ✅ Verify folder isn't excluded
- ✅ Check Synology has enough space
- ✅ Look at Remotely Save logs (Settings → View Logs)

### Conflicts appearing
- ✅ Change sync strategy to "Last modified wins"
- ✅ Ensure time is synced on all devices
- ✅ Don't edit same note simultaneously on multiple devices

---

## Daily Workflow

### On Mac:
1. **Work in Obsidian normally**
2. **Remotely Save auto-syncs every 10 minutes**
3. **Cron job runs weekly** (Sundays 9 AM):
   - Copies new screenshots → Obsidian
   - Copies new AI chats → Obsidian
   - Remotely Save then syncs to Synology

### On iPhone:
1. **Open Obsidian app**
2. **Remotely Save auto-syncs** on open
3. **Take notes, capture thoughts**
4. **Syncs in background every 10 minutes**

### Result:
- All devices always have latest vault
- 30-60 second sync delay (acceptable)
- No file size limits
- No monthly fees
- Full control of your data

---

## Advanced: Selective Sync for iPhone

If vault is too large for iPhone storage:

1. **Settings → Remotely Save → Advanced**
2. **Exclude large folders on mobile:**
   ```
   Apple Notes/Archive/
   Screenshots/
   Attachments/AI Chats/
   ```

3. **iPhone only syncs:**
   - Active notes
   - Current year Apple Notes
   - Recent AI chats

4. **Mac has full vault**

---

## Backup Strategy

Your sync setup provides 3 copies of data:

1. **Mac (Primary):** `/Users/KevinHG/Documents/HG Main/`
2. **Synology (Backup 1):** WebDAV folder
3. **iPhone (Backup 2):** Obsidian mobile vault

**Additional backup (recommended):**
- Enable Synology **Hyper Backup** to backup `/Obsidian/` folder
- To external drive or cloud (one-way backup)
- Protects against ransomware/accidental deletion

---

## Cost Comparison

| Solution | Setup Time | Monthly Cost | Storage Limit | File Size Limit |
|----------|------------|--------------|---------------|-----------------|
| **Remotely Save + Synology** | 20 min | $0 | Unlimited* | None |
| Obsidian Sync Standard | 2 min | $4 | 10GB | 5MB |
| Obsidian Sync Plus | 2 min | $8 | 100GB | 200MB |
| Dropbox | 5 min | $12 | 2TB | None |

*Unlimited = Limited only by your Synology drive capacity

---

## Need Help?

**Check logs:**
```bash
# Cron sync log
tail -50 ~/.obsidian_sync_log.txt

# Remotely Save logs
# Settings → Remotely Save → View Logs
```

**Test manual sync:**
```bash
cd ~/.cmux/src/hello-world/qna/scripts
./weekly_obsidian_sync.sh
```

**View cron jobs:**
```bash
crontab -l
```

**Reinstall cron:**
```bash
cd ~/.cmux/src/hello-world/qna/scripts
./uninstall_cron_jobs.sh
./install_cron_jobs.sh
```

---

## Summary

✅ **Free** - No monthly subscription  
✅ **Unlimited** - Only limited by your NAS  
✅ **Private** - Your data stays on your hardware  
✅ **Fast** - Local network = fast sync  
✅ **Flexible** - Works on Mac, iPhone, iPad  
✅ **Reliable** - Synology hardware is enterprise-grade  

You now have a professional-grade sync solution that costs nothing per month and gives you complete control!

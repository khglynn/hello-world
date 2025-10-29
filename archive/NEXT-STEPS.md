# 🎯 Next Steps - Getting Started with n8n

Congratulations! Your n8n setup is ready. Here's what to do next:

## ✅ Step 1: Install Prerequisites

You need to install these before n8n can run:

### A. Docker Desktop (Required)
1. Go to: https://www.docker.com/products/docker-desktop/
2. Download for Mac (choose your chip: Apple Silicon or Intel)
3. Install and start Docker Desktop
4. Wait for the whale icon to appear in your menu bar

**Verify it works:**
```bash
docker --version
docker compose version
```

### B. VS Code (Recommended)
1. Go to: https://code.visualstudio.com/
2. Download for macOS
3. Install to Applications folder
4. Open this project folder in VS Code

**Optional - Install VS Code from terminal:**
1. First install Homebrew (if not already):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Then install VS Code:
   ```bash
   brew install --cask visual-studio-code
   ```

---

## ✅ Step 2: Configure Your Setup

1. **Edit the `.env` file:**
   ```bash
   # Open in your editor
   nano .env
   # or
   code .env
   ```

2. **Change the password** (important for security!):
   ```env
   N8N_PASSWORD=YourSecurePassword123!
   ```

3. **Adjust timezone** (optional):
   Find your timezone: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
   ```env
   TIMEZONE=America/Los_Angeles  # or your timezone
   ```

---

## ✅ Step 3: Start n8n

Once Docker Desktop is running:

### Option A: Use the Quick Start Script (Easiest)
```bash
./quick-start.sh
```

This will:
- Check if Docker is running
- Create necessary directories
- Start n8n
- Show you the access URL

### Option B: Manual Start
```bash
# Start n8n in the background
docker compose up -d

# View logs (optional)
docker compose logs -f
```

---

## ✅ Step 4: Access n8n

1. Open your browser
2. Go to: **http://localhost:5678**
3. Log in with:
   - Username: `admin`
   - Password: (from your `.env` file)

4. Complete the initial setup:
   - Create an owner account (additional to basic auth)
   - Skip cloud features if you don't need them
   - Start creating workflows!

---

## ✅ Step 5: Add Your Notes

Put your notes in the `notes/` folder:

```bash
# Example: Copy notes from somewhere
cp ~/Documents/MyNotes/*.md ./notes/

# Or create a test note
echo "# My First Note" > notes/test.md
```

There's already an example note in `notes/example-note.md` to help you get started.

---

## ✅ Step 6: Create Your First Workflow

### Simple Test Workflow:
1. In n8n, click "Add Workflow"
2. Add these nodes:
   - **Manual Trigger** (to start the workflow manually)
   - **Read Binary Files** node
     - Set File Selector: `/notes/*.md`
   - **Extract from File** node
     - To convert binary to text
   - **Code** node (to process the text)
     - Add simple JavaScript to count words

3. Click "Test Workflow"
4. See your notes processed!

### Pre-built Examples:
Check **WORKFLOW-EXAMPLES.md** for 8 ready-to-use workflows:
- Note Organizer
- Tag Extractor  
- Markdown to HTML Converter
- AI Summarizer
- And more!

---

## 🎓 Learning Resources

### Essential Docs:
- **n8n Docs:** https://docs.n8n.io/
- **Workflow Gallery:** https://n8n.io/workflows
- **YouTube Channel:** https://www.youtube.com/c/n8n-io

### Community:
- **Forum:** https://community.n8n.io/
- **Discord:** https://discord.gg/n8n

---

## 🔧 Useful Commands Reference

```bash
# Check if n8n is running
docker compose ps

# Start n8n
docker compose up -d

# Stop n8n
docker compose down

# Restart n8n
docker compose restart

# View logs (live)
docker compose logs -f

# View last 50 log lines
docker compose logs --tail=50

# Update to latest n8n version
docker compose pull
docker compose up -d

# Backup workflows
# (Or export from n8n UI: Settings → Export)
docker compose exec n8n n8n export:workflow --all --output=/backups/workflows.json
```

---

## 🎯 Quick Wins - Try These First

1. **Basic File Reader:**
   - Manual Trigger → Read Binary Files (`/notes/*.md`)
   - Test: See all your notes appear

2. **Tag Counter:**
   - Read notes → Extract from File → Code node
   - Count hashtags and create summary

3. **Auto-Organizer:**
   - Schedule Trigger (daily) → Read Files → Code (add date prefix) → Write File
   - Automatically organize notes by date

---

## 🐛 Troubleshooting

### Docker won't start
- Make sure Docker Desktop is installed and running
- Check for whale icon in menu bar
- Try: `docker ps` to verify

### Can't access localhost:5678
- Wait 30 seconds after starting (first start takes time)
- Check logs: `docker compose logs`
- Check container: `docker compose ps`
- Try restarting: `docker compose restart`

### Workflow can't read files
- Verify notes exist: `ls -la notes/`
- Check paths in workflow (use `/notes/` not `./notes/`)
- Restart container: `docker compose restart`

---

## 📞 Need Help?

1. **Check INSTALLATION.md** - Comprehensive guide with detailed troubleshooting
2. **Check WORKFLOW-EXAMPLES.md** - 8 example workflows with code
3. **Check logs:** `docker compose logs`
4. **Community forum:** https://community.n8n.io/

---

## 🎉 You're All Set!

The hard part is done. Now comes the fun part:
- Experiment with workflows
- Automate your note processing
- Build custom solutions for your needs

**Remember:** Start simple, test often, and iterate!

Happy automating! 🚀

---

## 📋 Quick Checklist

- [ ] Docker Desktop installed and running
- [ ] VS Code installed (optional)
- [ ] Changed password in `.env` file
- [ ] Started n8n with `./quick-start.sh`
- [ ] Accessed http://localhost:5678
- [ ] Created owner account in n8n
- [ ] Added notes to `notes/` folder
- [ ] Created first test workflow
- [ ] Explored WORKFLOW-EXAMPLES.md
- [ ] Joined n8n community (optional)

Once you've checked these off, you're ready to rock! 🎸


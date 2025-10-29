# n8n Installation Guide for Note Processing

This guide will help you set up n8n locally on your macOS system for processing and organizing notes.

## 📋 Prerequisites

Before starting, you need to install:

### 1. Docker Desktop (Required)

Docker Desktop is needed to run n8n in a container.

**Installation Steps:**
1. Download Docker Desktop for Mac (Apple Silicon or Intel):
   - Visit: https://www.docker.com/products/docker-desktop/
   - Click "Download for Mac"
   - Choose the right version for your Mac chip (Apple Silicon M1/M2/M3 or Intel)

2. Install Docker Desktop:
   - Open the downloaded `.dmg` file
   - Drag Docker.app to Applications folder
   - Launch Docker from Applications
   - Complete the initial setup wizard
   - Accept the service agreement

3. Verify Installation:
   ```bash
   docker --version
   docker compose version
   ```
   You should see version numbers (e.g., Docker version 24.x.x)

4. **Important:** Keep Docker Desktop running (you'll see a whale icon in your menu bar)

### 2. VS Code (Optional but Recommended)

Visual Studio Code is the best editor for working with workflows and configuration files.

**Installation Steps:**
1. Visit: https://code.visualstudio.com/
2. Click "Download for macOS"
3. Open the downloaded `.zip` file
4. Drag "Visual Studio Code.app" to Applications folder
5. Launch VS Code from Applications

**Recommended VS Code Extensions:**
- Install these after opening VS Code:
  - Docker (by Microsoft) - for managing containers
  - YAML (by Red Hat) - for editing docker-compose.yml
  - Markdown All in One - for note documentation
  - GitLens - for version control

  To install: Press `Cmd+Shift+X` and search for each extension

### 3. Homebrew (Optional - for easier tool management)

While not required, Homebrew makes installing tools easier:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the on-screen instructions. After installation, you can use:
```bash
brew install --cask docker
brew install --cask visual-studio-code
```

---

## 🚀 Starting n8n

Once Docker Desktop is installed and running:

### Step 1: Configure Your Environment

1. Open the `.env` file in this directory
2. **Change the password** (security best practice!):
   ```env
   N8N_PASSWORD=YourSecurePassword123!
   ```
3. Adjust timezone if needed (find yours at: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

### Step 2: Start n8n

Open Terminal in this directory and run:

```bash
docker compose up -d
```

**What this does:**
- Downloads the n8n Docker image (first time only, ~200MB)
- Creates a container named "n8n"
- Starts n8n in the background
- Makes it accessible at http://localhost:5678

### Step 3: Access n8n

1. Open your browser and go to: http://localhost:5678
2. Log in with credentials from your `.env` file:
   - Username: `admin` (or what you set)
   - Password: Your password from `.env`

### Step 4: Create Your First Workflow

On first login, n8n will guide you through:
1. Creating an owner account (additional to basic auth)
2. Setting up your first workflow
3. Optional: Sign up for n8n cloud features (can skip)

---

## 📁 Directory Structure

```
n8n/
├── docker-compose.yml      # Docker configuration
├── .env                    # Your configuration (passwords, etc.)
├── .env.example           # Template for configuration
├── notes/                 # Put your notes here (read-only to n8n)
├── processed/             # n8n will output processed notes here
├── backups/               # For workflow backups
└── INSTALLATION.md        # This file
```

**Important Volume Mappings:**
- `./notes` → Container sees as `/notes` (read-only)
- `./processed` → Container sees as `/processed` (read-write)
- `./backups` → Container sees as `/backups` (read-write)

---

## 🔧 Common Commands

### Start n8n
```bash
docker compose up -d
```

### Stop n8n
```bash
docker compose down
```

### View logs
```bash
docker compose logs -f
```

### Restart n8n
```bash
docker compose restart
```

### Update n8n to latest version
```bash
docker compose pull
docker compose up -d
```

### Check if n8n is running
```bash
docker compose ps
```

---

## 📝 Setting Up Note Processing

### 1. Add Your Notes

Place your notes in the `notes/` directory:
```bash
# Example: Copy notes from your Documents folder
cp -r ~/Documents/MyNotes/* ./notes/
```

### 2. Example Workflow Ideas

In n8n, you can create workflows to:

**Basic Organization:**
- Monitor `notes/` folder for new files
- Read file content
- Extract tags or keywords
- Organize into folders in `processed/`
- Rename files with date prefixes

**Advanced Processing:**
- Extract text from PDFs
- Convert between formats (Markdown ↔ HTML)
- Generate summaries using AI
- Create search indexes
- Sync with cloud services (Notion, Google Drive, etc.)

### 3. File Access in Workflows

In n8n workflows, use these paths:
- Read notes from: `/notes/`
- Write processed files to: `/processed/`
- Save backups to: `/backups/`

---

## 🔐 Security Notes

1. **Change the default password** in `.env` before starting
2. The `.env` file is in `.gitignore` - don't commit it!
3. For production use, consider:
   - Setting up HTTPS
   - Using stronger authentication
   - Backing up the `n8n_data` volume regularly

---

## 🆘 Troubleshooting

### n8n won't start
- **Check Docker is running:** Look for whale icon in menu bar
- **Check logs:** `docker compose logs`
- **Port already in use:** Change port in docker-compose.yml (5678 → something else)

### Can't access http://localhost:5678
- Wait 30 seconds after starting (initial startup takes time)
- Check container is running: `docker compose ps`
- Try: `docker compose restart`

### Workflows can't see my notes
- Check files exist: `ls -la notes/`
- Verify volume mapping in docker-compose.yml
- Restart container: `docker compose restart`

### "Permission denied" errors
- Check directory permissions: `ls -la`
- Try: `chmod -R 755 notes/ processed/ backups/`

---

## 🎓 Next Steps

1. **Learn n8n Basics:**
   - Official docs: https://docs.n8n.io/
   - Video tutorials: https://www.youtube.com/c/n8n-io

2. **Explore Nodes:**
   - File system operations (Read/Write Binary Files)
   - Text processing (Split, Extract, Transform)
   - Conditional logic (IF, Switch)
   - Loops (Loop Over Items)

3. **Join Community:**
   - Forum: https://community.n8n.io/
   - Discord: https://discord.gg/n8n

---

## 📦 Backup Your Work

### Export Workflows
In n8n UI: Settings → Export → Download workflows

### Backup Data Volume
```bash
docker run --rm -v n8n_n8n_data:/data -v $(pwd)/backups:/backup \
  alpine tar czf /backup/n8n-backup-$(date +%Y%m%d).tar.gz -C /data .
```

### Restore from Backup
```bash
docker run --rm -v n8n_n8n_data:/data -v $(pwd)/backups:/backup \
  alpine tar xzf /backup/your-backup-file.tar.gz -C /data
```

---

## 🤝 Need Help?

- Check the logs: `docker compose logs`
- Review n8n docs: https://docs.n8n.io/
- Ask questions in this project's issues
- Community forum: https://community.n8n.io/

Happy automating! 🎉


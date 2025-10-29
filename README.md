# 🚀 n8n Note Processing Setup

> **Complete n8n installation for automated note processing and organization**

[![n8n](https://img.shields.io/badge/n8n-latest-orange)](https://n8n.io)
[![Docker](https://img.shields.io/badge/docker-required-blue)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 🎯 What is This?

This is a **production-ready n8n setup** for processing and organizing notes locally on your Mac. It includes:

- ✅ Docker Compose configuration with best practices
- ✅ Pre-configured environment with security settings
- ✅ Persistent data storage and volume mappings
- ✅ 8 example workflows for note processing
- ✅ Comprehensive documentation
- ✅ Quick-start script for easy setup

---

## ⚡ Quick Start (3 Steps)

### 1. Install Prerequisites

**Docker Desktop (Required):**
```bash
# Download from: https://www.docker.com/products/docker-desktop/
# Or install via Homebrew:
brew install --cask docker
```

**VS Code (Optional but Recommended):**
```bash
# Download from: https://code.visualstudio.com/
# Or install via Homebrew:
brew install --cask visual-studio-code
```

### 2. Configure & Start

```bash
# 1. Edit the .env file and change the password
nano .env  # or use VS Code

# 2. Start n8n
./quick-start.sh
```

### 3. Access n8n

Open http://localhost:5678 in your browser
- Username: `admin`
- Password: (from your `.env` file)

**That's it!** 🎉

---

## 📁 What's Included

```
n8n/
├── 📄 docker-compose.yml        Docker configuration with best practices
├── 🔐 .env                      Your configuration (CHANGE PASSWORD!)
├── 🔐 .env.example              Template for configuration
├── 📝 README.md                 This file
├── 📚 INSTALLATION.md           Complete installation guide (285 lines)
├── 💡 WORKFLOW-EXAMPLES.md      8 example workflows with code
├── 🎯 NEXT-STEPS.md             Step-by-step getting started
├── 🚀 quick-start.sh            One-command startup script
├── 📁 notes/                    Put your notes here (read-only to n8n)
│   └── example-note.md          Sample note to test workflows
├── 📁 processed/                n8n outputs processed notes here
└── 📁 backups/                  For workflow and data backups
```

---

## 🛠️ Common Commands

```bash
# Start n8n (detached)
docker compose up -d

# Stop n8n
docker compose down

# View logs
docker compose logs -f

# Restart n8n
docker compose restart

# Check status
docker compose ps

# Update to latest version
docker compose pull && docker compose up -d
```

---

## 💡 Example Workflows

This setup includes 8 ready-to-use workflow examples:

1. **📋 Simple Note Organizer** - Auto-organize notes with date prefixes
2. **🏷️ Tag Extractor** - Extract and index all hashtags
3. **🔍 Note Deduplicator** - Find and remove duplicate notes
4. **📝 Markdown to HTML** - Convert notes for publishing
5. **🤖 AI Summarizer** - Generate summaries using OpenAI/Claude
6. **📧 Daily Digest** - Create daily note summaries
7. **☁️ Cloud Backup** - Auto-backup to Google Drive/Dropbox/S3
8. **🔎 Search Index** - Create searchable index of all notes

**See WORKFLOW-EXAMPLES.md for complete code and instructions!**

---

## 🎓 Documentation

| Document | Description |
|----------|-------------|
| **INSTALLATION.md** | Complete installation guide with prerequisites, troubleshooting, and security tips |
| **WORKFLOW-EXAMPLES.md** | 8 example workflows with code, tips, and best practices |
| **NEXT-STEPS.md** | Step-by-step guide from installation to your first workflow |

---

## 🔐 Security Notes

1. ⚠️ **Change the default password** in `.env` before starting
2. ✅ The `.env` file is in `.gitignore` (won't be committed)
3. 🔒 Basic authentication is enabled by default
4. 🛡️ For production, consider HTTPS and stronger authentication

---

## 📝 Using with Your Notes

### Add Notes to Process

```bash
# Copy your existing notes
cp -r ~/Documents/MyNotes/*.md ./notes/

# Or create new ones
echo "# My Note" > notes/my-note.md
```

### Access in Workflows

In n8n workflows, use these paths:
- **Read notes from:** `/notes/`
- **Write processed files to:** `/processed/`
- **Save backups to:** `/backups/`

---

## 🆘 Troubleshooting

### n8n won't start
```bash
# Check Docker is running (look for whale icon in menu bar)
docker ps

# View logs
docker compose logs

# Try restarting
docker compose restart
```

### Can't access localhost:5678
```bash
# Wait 30 seconds after starting (initial startup takes time)
sleep 30

# Check if container is healthy
docker compose ps

# Check logs for errors
docker compose logs n8n
```

### Workflows can't see notes
```bash
# Verify files exist
ls -la notes/

# Check permissions
chmod -R 755 notes/

# Restart container
docker compose restart
```

**For more help, see INSTALLATION.md**

---

## 🌟 Features

- **🐳 Docker-based:** Isolated, portable, easy to manage
- **💾 Persistent Storage:** Data survives container restarts
- **📁 Volume Mapping:** Easy access to notes and processed files
- **🔄 Auto-restart:** Container restarts automatically on failure
- **🏥 Health Checks:** Monitors n8n availability
- **🔒 Security:** Basic auth enabled by default
- **📊 Best Practices:** Production-ready configuration
- **📚 Comprehensive Docs:** Everything you need to know

---

## 🔗 Resources

- **n8n Documentation:** https://docs.n8n.io/
- **n8n Workflow Templates:** https://n8n.io/workflows
- **Community Forum:** https://community.n8n.io/
- **Discord:** https://discord.gg/n8n
- **YouTube Tutorials:** https://www.youtube.com/c/n8n-io

---

## 📦 Backup & Restore

### Export Workflows
```bash
# From n8n UI: Settings → Export → Download
# Or via command:
docker compose exec n8n n8n export:workflow --all --output=/backups/workflows.json
```

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

## 🤝 Contributing

Found a bug or have a suggestion? Feel free to:
- Open an issue
- Submit a pull request
- Share your workflows

---

## 📜 License

This setup is provided as-is under the MIT License. n8n itself is licensed under the [Sustainable Use License](https://github.com/n8n-io/n8n/blob/master/LICENSE.md).

---

## 🎉 Credits

- **n8n:** https://n8n.io - The workflow automation platform
- **Docker:** https://www.docker.com - Containerization platform

---

## 💬 Support

Need help?
1. Check **NEXT-STEPS.md** for getting started
2. Check **INSTALLATION.md** for troubleshooting
3. Check **WORKFLOW-EXAMPLES.md** for examples
4. Visit the [n8n community forum](https://community.n8n.io/)

---

<div align="center">

### Ready to automate your notes? 🚀

**[Read NEXT-STEPS.md →](NEXT-STEPS.md)**

Made with ❤️ for note-takers and automation enthusiasts

</div>


# 📦 Installing Docker Desktop and VS Code

Quick reference for installing the prerequisites on macOS.

## Method 1: Direct Downloads (Recommended for Beginners)

### Docker Desktop
1. Go to: https://www.docker.com/products/docker-desktop/
2. Click "Download for Mac"
3. Choose your Mac type:
   - **Apple Silicon** (M1/M2/M3/M4) - for newer Macs
   - **Intel** - for older Macs (pre-2020)
4. Open the downloaded `.dmg` file
5. Drag Docker.app to Applications
6. Launch Docker from Applications
7. Complete setup wizard and accept terms
8. Wait for Docker to start (whale icon in menu bar)

**Verify installation:**
```bash
docker --version
docker compose version
```

### VS Code
1. Go to: https://code.visualstudio.com/
2. Click "Download for macOS"
3. Open the downloaded `.zip` file
4. Drag "Visual Studio Code.app" to Applications
5. Launch VS Code from Applications
6. Open this project: File → Open Folder → select `n8n` folder

**Recommended Extensions (optional):**
- Docker (by Microsoft)
- YAML (by Red Hat)
- Markdown All in One

Install by pressing `Cmd+Shift+X` in VS Code and searching.

---

## Method 2: Homebrew (For Advanced Users)

If you don't have Homebrew installed:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install Docker and VS Code:
```bash
# Install Docker Desktop
brew install --cask docker

# Install VS Code
brew install --cask visual-studio-code

# Verify installations
docker --version
code --version
```

---

## After Installation

1. **Start Docker Desktop** - Open from Applications, wait for whale icon
2. **Change password** - Edit `.env` file in this directory
3. **Start n8n** - Run `./quick-start.sh`
4. **Open browser** - Go to http://localhost:5678

---

## Troubleshooting

### Docker Desktop won't start
- Check System Requirements (macOS 11 or later)
- Make sure you have at least 4GB RAM available
- Check Activity Monitor for conflicts
- Try: Restart Mac, then launch Docker Desktop again

### VS Code command 'code' not found
- In VS Code: Press `Cmd+Shift+P`
- Type: "Shell Command: Install 'code' command in PATH"
- Press Enter
- Restart terminal

---

Need more help? See INSTALLATION.md or NEXT-STEPS.md

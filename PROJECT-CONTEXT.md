# 🎯 Project Context: Apple Notes → Notion Automation

> **Last Updated:** 2025-10-29  
> **Status:** n8n installed and running, ready for workflow development  
> **Next Session:** Build Apple Notes → LLM → Notion workflow

---

## 📋 Project Overview

### Goal
Automate processing of Apple Notes into a structured Notion database with AI-powered categorization and human review.

### Workflow Architecture

```
📱 Apple Notes (local)
  ↓ Export to text files
☁️  Google Drive (backup, optional)
  ↓
📂 /notes/ folder (n8n reads from here)
  ↓
🤖 LLM Processing (OpenRouter/OpenAI)
  ├─ Split notes into sections
  ├─ Categorize (3-layer structure)
  ├─ Extract properties
  └─ Generate embeddings
  ↓
👤 Human-in-the-Loop Review
  ├─ Confirm/edit categories
  ├─ Approve/reject splits
  └─ Adjust properties
  ↓
📤 Dual Output:
  ├─ 📊 Notion Database (human-readable, 3-layer structure)
  └─ 🧠 Vector DB (AI-optimized) + PostgreSQL (backup)
```

---

## ✅ What's Done

### Infrastructure
- ✅ n8n installed via Docker (v1.117.3)
- ✅ Running at http://localhost:5678
- ✅ Docker Compose configuration with best practices
- ✅ Directory structure: `/notes/`, `/processed/`, `/backups/`
- ✅ Example workflows created and importable
- ✅ Documentation consolidated

### Configuration Files
- ✅ `docker-compose.yml` - Production-ready n8n setup
- ✅ `.env` - Configuration (password needs changing!)
- ✅ `.gitignore` - Protects secrets
- ✅ `quick-start.sh` - One-command startup

### Workflows Available
- ✅ `starter-note-processor.json` - Basic note reading and metadata extraction
- ✅ `openrouter-ai-example.json` - AI integration example

---

## 🎯 What's Needed Next

### 1. User Input Required

**3-Layer Category Structure:**
- Level 1: ? (e.g., Personal, Work, Learning)
- Level 2: ? (depends on Level 1)
- Level 3: ? (depends on Level 2)
- User mentioned having past research on this - needs to be shared

**Technology Decisions:**
- [ ] LLM Provider: OpenRouter (likely), which models?
- [ ] Vector Database: Pinecone (cloud) or Weaviate (local)?
- [ ] Human-Readable DB: PostgreSQL or just use Notion?
- [ ] HITL Interface: n8n form, Airtable, or Notion-based?

**API Keys/Credentials:**
- [ ] OpenRouter API key
- [ ] Notion API token + Database ID
- [ ] Google Drive (optional, for backup)
- [ ] Vector DB credentials

### 2. Technical Setup

**To Build:**
- [ ] Main processing workflow (Apple Notes → Notion)
- [ ] Duplicate detection logic
- [ ] LLM categorization prompts (needs category structure)
- [ ] Human review interface
- [ ] Notion database schema
- [ ] Vector DB integration
- [ ] PostgreSQL schema (if chosen)

**Optional Additions:**
- [ ] Add PostgreSQL to docker-compose.yml
- [ ] Add Weaviate for local vector DB
- [ ] Backup workflow (to Google Drive)
- [ ] Search workflow (query vector DB)

---

## 💾 Current Setup Details

### Location
- Main folder: `/Users/KevinHG/hello-world`
- cmux workspace: `/Users/KevinHG/.cmux/src/hello-world/n8n`
- GitHub: `https://github.com/khglynn/hello-world` (public)

### n8n Access
- URL: http://localhost:5678
- Username: `admin`
- Password: `changeme123!` (in `.env` file - should be changed!)
- Container: `n8n` (managed via docker compose)

### Secrets (cmux)
- Location: `~/.cmux/secrets.json`
- Current: ANTHROPIC key only
- Need to add: OpenRouter, Notion, etc.

### Commands
```bash
# Start n8n
cd /Users/KevinHG/hello-world
docker compose up -d
# or: /usr/local/bin/docker compose up -d

# Stop n8n
docker compose down

# View logs
docker compose logs -f

# Check status
docker compose ps
```

---

## 📚 Key Documents to Reference

### Essential Files (Keep These)
1. **PROJECT-CONTEXT.md** (this file) - Project state and next steps
2. **YOUR-ACTUAL-WORKFLOW.md** - Technical workflow design
3. **WORKFLOW-EXAMPLES.md** - Code snippets and examples
4. **docker-compose.yml** - Infrastructure config

### Reference Files (When Needed)
- **INSTALLATION.md** - If you need to reinstall or troubleshoot
- **ANSWERS-TO-YOUR-QUESTIONS.md** - Tonight's Q&A reference

### Can Archive/Delete
- README.md (generic intro, can regenerate)
- START-HERE.md (first-time setup, already done)
- NEXT-STEPS.md (installation steps, already done)
- INSTALL-DOCKER-AND-VSCODE.md (already installed)
- HOW-TO-IMPORT-WORKFLOWS.md (one-time instructions)

---

## 🎓 Lessons Learned Tonight

### cmux Workflow
- cmux uses git worktrees (separate folders per branch)
- Secrets stored in `~/.cmux/secrets.json` (project-scoped)
- Terminal commands can run in chat, but separate terminal is useful
- Files created in worktree need to be merged to master to appear in main folder

### Git Workflow for Solo Projects
- Branches add complexity
- Working on master is simpler
- cmux auto-creates branches for isolation
- Need to merge or work directly on master going forward

### n8n Setup
- Docker credential issues require PATH fixes
- First image pull takes 2-5 minutes
- Health checks confirm when ready
- Free version has everything needed for this project

### Enterprise Features
- Variables, Data Tables, Advanced Insights = not needed
- Can use PostgreSQL, Notion, or external databases instead
- Free version sufficient for Apple Notes → Notion workflow

---

## 🚀 Quick Start for Next Session

### If Continuing This Workspace:
```
1. Review PROJECT-CONTEXT.md
2. Share 3-layer category structure
3. Get API keys (OpenRouter, Notion)
4. Build main workflow together
```

### If Starting Fresh Workspace:
```
1. Reference this file for context
2. Clone or use existing n8n setup
3. Continue from "What's Needed Next" section
```

### If Using Different AI Interface:
- **VS Code Chat:** Reference this file + share technical requirements
- **Claude Web:** Upload this file as project context
- **AI within n8n:** Use for workflow-specific help, not project planning

---

## 🔑 Key Technical Decisions Pending

1. **LLM Strategy:**
   - Which models for categorization vs summarization?
   - Token budget per note?
   - Fallback models if primary fails?

2. **Database Strategy:**
   - Add PostgreSQL to docker-compose? (recommended for duplicate detection)
   - Use Notion as primary DB? (simpler, already going there)
   - Need separate vector DB or embed in PostgreSQL? (pgvector extension)

3. **HITL Strategy:**
   - n8n webhook + simple form?
   - Airtable interface?
   - Review in Notion directly?

4. **Duplicate Detection:**
   - Content hash based?
   - Semantic similarity via vectors?
   - Title + date matching?

---

## 📞 Questions for Next Session

1. Share your 3-layer organizational structure
2. Share any existing research/ideation on this project
3. Preferred LLM: GPT-4, Claude, or mix?
4. Want PostgreSQL added to docker-compose?
5. Have you created the Notion database yet?

---

## 🛠️ Technical Notes

### n8n Limitations to Know
- No built-in vector database (use external)
- No built-in semantic search (use LLM or vector DB)
- Enterprise variables not available (use env vars or DB)
- Data tables locked (use PostgreSQL)

### Recommended Stack (All Free)
- **n8n:** Workflow orchestration (already running)
- **OpenRouter:** LLM access (gpt-4-turbo recommended)
- **Notion:** Final storage + human DB
- **PostgreSQL:** Temp storage, duplicate detection (can add)
- **Pinecone:** Vector DB for AI search (1M vectors free)

### Optional Enhancements
- Weaviate for local vector DB (privacy)
- Supabase instead of PostgreSQL (hosted)
- Airtable for HITL review (visual interface)

---

## 📝 Session Summary (2025-10-29)

**Accomplished:**
- Set up n8n with Docker ✅
- Created comprehensive documentation ✅
- Merged git branches (understood worktrees) ✅
- Got n8n running and accessible ✅
- Created importable workflow examples ✅
- Answered all questions about enterprise/AI ✅

**Time Invested:** ~1 hour
**Lines of Documentation:** 2,460+ lines
**Workflows Created:** 2 importable examples
**Ready for:** Building the actual Apple Notes → Notion workflow

---

**Next session: Share category structure and build the real workflow!** 🚀


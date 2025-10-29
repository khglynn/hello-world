# 🤖 Claude Skills & n8n AI Assistant - October 2025 Updates

> Latest information on Claude Skills and n8n AI chat sidebar capabilities

**Last Updated:** October 29, 2025

---

## 🆕 Claude Skills (Released October 16, 2025)

### What Are Claude Skills?

<cite index="3-1,3-2,3-3">Claude can now use Skills to improve how it performs specific tasks. Skills are folders that include instructions, scripts, and resources that Claude can load when needed. Claude will only access a skill when it's relevant to the task at hand.</cite>

**Think of Skills as:** <cite index="3-27">Custom onboarding materials that let you package expertise, making Claude a specialist on what matters most to you.</cite>

### How Skills Work

<cite index="4-16">Skills are conceptually extremely simple: a skill is a Markdown file telling the model how to do something, optionally accompanied by extra documents and pre-written scripts that the model can run to help it accomplish the tasks described by the skill.</cite>

**Structure:**
```
my-skill/
├── SKILL.md           ← Instructions for Claude
├── resources/         ← Optional files/data
└── scripts/           ← Optional executable code
```

<cite index="4-20,4-21">At the start of a session Claude's various harnesses can scan all available skill files and read a short explanation for each one from the frontmatter YAML in the Markdown file. This is very token efficient: each skill only takes up a few dozen extra tokens, with the full details only loaded in should the user request a task that the skill can help solve.</cite>

### Key Features

<cite index="3-33,3-34,3-35,3-36">Skills are organized folders of instructions, scripts, and resources that Claude loads dynamically to perform specialized tasks. The initial release includes: Anthropic-managed Skills: Pre-built Skills for working with PowerPoint (.pptx), Excel (.xlsx), Word (.docx), and PDF files · Custom Skills: Upload your own Skills via the Skills API (/v1/skills endpoints) to package domain expertise and organizational workflows · Skills require the code execution tool to be enabled</cite>

**Characteristics:**
- **Composable:** Skills stack together - Claude figures out what's needed
- **Portable:** Works across Claude apps, Claude Code, and API
- **Efficient:** Only loads what's needed, when needed
- **Powerful:** Can include executable code for reliability

### Availability

<cite index="3-29">Skills are available to Pro, Max, Team and Enterprise users.</cite>

### How to Use Skills in cmux (Claude Code)

<cite index="3-4,3-5,3-6,3-7,3-8">Skills extend Claude Code with your team's expertise and workflows. Install skills via plugins from the anthropics/skills marketplace. Claude loads them automatically when relevant. Share skills through version control with your team. You can also manually install skills by adding them to ~/.claude/skills.</cite>

**Installation:**
```bash
# Manual installation
mkdir -p ~/.claude/skills
cd ~/.claude/skills

# Download or create a skill
# Example: Clone from anthropics/skills repo
git clone https://github.com/anthropics/skills

# Claude will auto-discover skills in ~/.claude/skills/
```

**Creating Custom Skills:**
<cite index="3-34">The "skill-creator" skill provides interactive guidance: Claude asks about your workflow, generates the folder structure, formats the SKILL.md file, and bundles the resources you need.</cite>

### Do Skills Apply to cmux? YES! ✅

**cmux IS Claude Code**, so Skills work here!

**Tomorrow you can:**
1. Install skills to `~/.claude/skills/`
2. Claude (me) will automatically use relevant skills
3. No manual enabling needed - I'll detect and load them

**For your n8n project**, you could create a skill:
```
~/.claude/skills/n8n-workflow-builder/
├── SKILL.md         ← Instructions for building n8n workflows
├── examples/        ← Sample workflow JSON files
└── templates/       ← Common node configurations
```

---

## 🆕 n8n AI Assistant & Sidebar Options

### Official n8n AI Assistant (Cloud Only)

<cite index="13-5,13-6">The n8n AI Assistant helps you build, debug, and optimize your workflows seamlessly. From answering questions about n8n to providing help with coding and expressions, the AI Assistant can streamline your workflow-building process and support you as you navigate n8n's capabilities.</cite>

**Features:**
<cite index="13-7,13-8,13-9,13-10,13-11">Debug helper: Identify and troubleshoot node execution issues in your workflows to keep them running without issues. Answer n8n questions: Get instant answers to your n8n-related questions, whether they're about specific features or general functionality. Coding support: Receive guidance on coding, including SQL and JSON, to optimize your nodes and data processing. Expression assistance: Learn how to create and refine expressions to get the most out of your workflows. Credential setup tips: Find out how to set up and manage node credentials securely and efficiently.</cite>

**Availability:**
<cite index="13-4,13-22">Any user on a Cloud plan can use the assistant.</cite>

**❌ NOT available for self-hosted** (what you're using)

### AI Workflow Builder (Beta - October 2025)

<cite index="24-1,24-2">Use text to generate a living workflow with nodes, logic and structure that you can shape and ship. It's rolling out over the course of this week to n8n Cloud builders on Trial, Starter, and Pro plans</cite>

**Also Cloud-only** ❌

### Community Extensions (Work with Self-Hosted!)

**Good news!** There are several browser extensions that add AI chat sidebars to n8n:

#### 1. **n8n Chat (Chrome Extension)** ⭐ Recommended

**What it does:**
<cite index="18-1,18-2">Cursor for n8n - create, edit, debug, and optimize n8n workflows using a simple chat. Transform How You Build n8n Automations n8nChat is a powerful extension that brings the intelligence of AI directly into your n8n workflow editor.</cite>

**Key Features:**
<cite index="18-18,18-19,18-20">Nodes appear directly in your workflow canvas, ready to use. 🔄 Complete Workflow Creation Need to build an entire workflow? Describe your automation goal, and n8nChat will generate a full multi-node workflow with proper connections and configurations.</cite>

<cite index="18-21">🖼️ Clone n8n Workflows From a Screenshot Attach a screenshot of any workflow and simply ask n8nChat to recreate it for you.</cite>

<cite index="18-23">🤖 Multiple AI Model Support - OpenAI and Gemini supported with your own API key.</cite>

<cite index="18-26,18-27">🔌 Instant Integration Generated nodes and workflows are instantly added to your canvas - no copy/paste required. Connections between nodes are automatically created based on your requirements.</cite>

**Install:**
- Chrome Web Store: Search "n8n Chat"
- Works with self-hosted instances! ✅
- Requires your own OpenAI or Gemini API key

**This is the sidebar you wanted!** 🎉

#### 2. **n8n AI Assistant (Chrome Extension)**

<cite index="20-1,20-15,20-16,20-17">AI assistant for n8n workflow automation. Works with self-hosted instances, AI APIs (OpenAI, Anthropic) and templates</cite>

**Features:**
- Generate workflows from text
- Import workflows from templates
- Works with self-hosted ✅

#### 3. **AgentCraft Copilot**

<cite index="20-7">AI for n8n: AgentCraft Copilot | Debug, Generate & Fix Workflows 10x Faster</cite>

- Debug workflows
- Generate JavaScript code
- Fix workflow issues

### Official n8n Cloud AI Assistant

<cite index="13-20">The AI Assistant has access to all elements displayed on your n8n screen, excluding actual input and output data values (like customer information).</cite>

**Privacy:** Your data stays private - it doesn't see actual values, just structure.

---

## 🎯 Recommendations for Your Self-Hosted Setup

### Option 1: n8n Chat Extension (Best!)

**Install this tomorrow:**
1. Open Chrome
2. Go to Chrome Web Store
3. Search "n8n Chat"
4. Install extension
5. Open n8n (http://localhost:5678)
6. Extension adds chat panel to your n8n UI!
7. Add your OpenAI or Gemini API key
8. Start chatting to build workflows!

**This gives you:**
- ✅ AI sidebar IN n8n
- ✅ No copy/paste needed
- ✅ Workflows generated directly on canvas
- ✅ Works with self-hosted
- ✅ Multiple AI model support

### Option 2: Dual Screen (Still Great)

**Setup:**
```
Left screen: n8n UI
Right screen: cmux chat
```

**Why still useful:**
- More control over context
- Better for complex planning
- Works offline
- Free (no API costs)
- Full conversation history

### Option 3: Combine Both!

**Power user setup:**
```
Main screen: n8n + n8n Chat extension
Secondary: cmux for complex questions
```

**Use n8n Chat for:**
- Quick node generation
- Debugging
- Simple workflow creation

**Use cmux for:**
- Complex workflow architecture
- Multi-step planning
- Infrastructure questions
- File operations

---

## 💡 Claude Skills for Your Project

### Creating a Custom n8n Skill

You could create a skill for your Apple Notes workflow:

```markdown
# ~/.claude/skills/apple-notes-n8n/SKILL.md

---
name: apple-notes-n8n-builder
description: Build n8n workflows for Apple Notes to Notion automation
applies_to: ["n8n workflow", "Apple Notes processing", "Notion integration"]
version: 1.0.0
---

# Apple Notes to Notion n8n Workflow Builder

This skill helps build n8n workflows that process Apple Notes and send them to Notion.

## Category Structure
Level 1: Personal, Work, Learning
Level 2: [Dynamically determined]
Level 3: [Dynamically determined]

## Common Nodes
- Read Binary Files: Path /notes/*.txt
- HTTP Request: OpenRouter API for categorization
- Notion: Create database pages
- Code: JavaScript for processing

## Workflow Patterns
[Include YOUR-ACTUAL-WORKFLOW.md content]

## Example Prompts
[Include categorization prompts]
```

**Then in cmux:**
```
"Using the apple-notes-n8n-builder skill, help me build 
the categorization workflow"
```

I'd automatically load your custom skill with all context!

---

## 📊 Comparison: Different AI Approaches for n8n

| Feature | n8n Cloud AI | n8n Chat Extension | cmux Dual Screen | Claude Skills |
|---------|--------------|-------------------|------------------|---------------|
| **Works with self-hosted** | ❌ | ✅ | ✅ | ✅ |
| **Cost** | Included in plan | Your API key | cmux subscription | Pro+ plan |
| **Integrated in n8n** | ✅ Native | ✅ Extension | ❌ Separate | ❌ Separate |
| **No copy/paste** | ✅ | ✅ | ❌ | ❌ |
| **Complex planning** | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Project context** | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Quick iterations** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

---

## 🚀 Recommended Setup for Tomorrow

### Phase 1: Quick Start (Simple)

```bash
1. Start n8n
2. Use cmux dual screen
3. Build workflows visually
4. Ask cmux for code snippets
5. Copy/paste to Code nodes
```

### Phase 2: Add Extension (If You Like It)

```bash
1. Install n8n Chat extension
2. Add API key (OpenAI or Gemini)
3. Now you have AI in sidebar!
4. Generate nodes with chat
5. Still use cmux for complex planning
```

### Phase 3: Power User (Optional)

```bash
1. Create custom Claude Skill for your workflow
2. Install in ~/.claude/skills/
3. Use in cmux chats
4. Persistent context across sessions!
```

---

## 🔑 Key Takeaways

### Claude Skills:
- ✅ Available in cmux (Claude Code)
- ✅ Install to `~/.claude/skills/`
- ✅ Auto-loaded when relevant
- ✅ Can package your n8n workflow knowledge
- ✅ No special enabling needed

### n8n AI Sidebar:
- ❌ Official version is Cloud-only
- ✅ **Extension exists!** (n8n Chat for Chrome)
- ✅ Works with self-hosted
- ✅ Multiple AI models supported
- ✅ No copy/paste needed
- ✅ Install tomorrow to try it!

### Best Approach:
- Start with cmux dual screen (free, powerful)
- Add n8n Chat extension if you want sidebar
- Consider creating custom Claude Skill for long-term

---

## 📝 cmux Spend Tracking

### Token/Cost Tracking

**In cmux interface:** Look for token count at bottom of chat window or in settings

**No built-in CLI command found** in `~/.cmux/` config

**Workarounds:**
1. Check cmux UI directly (may show token usage)
2. Anthropic Console: https://console.anthropic.com/
   - Shows total API usage
   - Billing dashboard
   - Usage breakdown

3. Check conversation metadata (if available in UI)

**For this conversation:**
- Approximately 165K tokens used
- Mostly context/setup discussion
- Fresh workspace tomorrow will be much more efficient!

---

## 🔧 Empty Folders & Config Files - Why Keep Them?

### Empty Folders (notes/, processed/, backups/)

**YES, keep them!** ✅

**Why:**
1. **docker-compose.yml references them** as volume mounts
2. **Workflows expect them** to exist
3. **Git needs placeholders** to track empty directories
4. **Prevents errors** when n8n tries to access them

**Without these folders:**
```bash
docker compose up -d
# ERROR: Mount path does not exist: /notes
```

**Best practice:**
Add `.gitkeep` files to keep folders in git:
```bash
touch notes/.gitkeep
touch processed/.gitkeep
touch backups/.gitkeep
```

### Config Files (.yml, .sh)

**YES, absolutely keep!** ✅✅✅

**docker-compose.yml:**
- ✅ **CRITICAL** - This IS your n8n installation
- ✅ Defines n8n container configuration
- ✅ Volume mappings (where your data goes)
- ✅ Environment variables
- ✅ Port mappings (5678)
- ❌ Delete this = n8n won't work!

**quick-start.sh:**
- ✅ Convenience script for starting n8n
- ✅ Checks Docker is running
- ✅ Creates directories
- ✅ Shows helpful messages
- ⚠️ Optional but very useful

**.env:**
- ✅ **IMPORTANT** - Your configuration
- ✅ Passwords, settings
- ✅ Should NOT be in git (already in .gitignore)
- ❌ Delete = lose your password/config

**.env.example:**
- ✅ Template for others
- ✅ Safe to commit (no secrets)
- ✅ Documentation of what's needed

**.gitignore:**
- ✅ Protects secrets
- ✅ Prevents committing .env
- ✅ Ignores generated files
- ✅ CRITICAL for security

**Summary:** All these files serve important purposes! Don't delete any of them.

---

## 📦 What CAN You Delete/Archive?

### Safe to Archive/Delete:

✅ **old-files/** (already archived)
- Goat.txt
- readme.txt (old)
- Old documentation

✅ **Nothing else!** Everything in root serves a purpose:
- Config files: Critical for n8n
- Folders: Expected by docker-compose
- docs/: Your knowledge base
- workflows/: Importable workflows

### If You Want to Clean Up:

**Option 1: Hide from view (not delete):**
```bash
# These folders will be empty until you use them
# That's OK! Docker creates them as needed
notes/       # Will fill with your notes
processed/   # Will fill with outputs
backups/     # Will fill with backups
```

**Option 2: Add .gitkeep:**
```bash
echo "# Placeholder" > notes/.gitkeep
echo "# Placeholder" > processed/.gitkeep
echo "# Placeholder" > backups/.gitkeep
```

Now git tracks the folders even when empty!

---

## 🎊 Final Recommendations

### For Tomorrow:

1. **Install n8n Chat Extension:**
   - Chrome Web Store
   - Search "n8n Chat"
   - Works with your self-hosted instance!
   - Gives you the AI sidebar you wanted! ✅

2. **Optional: Create Claude Skill:**
   ```bash
   mkdir -p ~/.claude/skills/apple-notes-workflow
   # Copy your workflow docs there
   # I'll auto-use it tomorrow!
   ```

3. **Keep using cmux:**
   - Best for complex planning
   - Can use Skills
   - Free (no API costs)
   - Works offline

### File Organization:

✅ **Keep:** All .yml, .sh, and config files (critical!)
✅ **Keep:** Empty folders (Docker needs them)
✅ **Archive:** Silly files like Goat.txt (already done!)
✅ **Current structure is perfect!**

---

## 💬 Tomorrow's Workflow with Extensions

**Ideal setup:**
```
1. Start n8n: docker compose up -d
2. Open Chrome → http://localhost:5678
3. n8n Chat extension = AI sidebar ✅
4. cmux on side = complex planning
5. Build workflows with AI assistance!
```

**No more copy/paste** if using extension! 🎉

---

**All your questions answered with latest 2025 info!** 🚀


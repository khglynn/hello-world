# 🤖 AI Tools Guide: Preparing Context for Different Interfaces

> How to optimize .md files and context for cmux, VS Code, Claude Web, and n8n AI

---

## 📋 Preparing .md Files for Different Tools

### General Best Practices (All Tools)

**Structure your .md files with:**
```markdown
# Title - What this is about

> Quick summary in italics

## Key sections with clear headings

### Subsections for details

**Bold for important points**

`Code in backticks`

```code blocks for longer code```

---

**Use horizontal rules to separate major sections**
```

**Why this matters:**
- AI reads markdown structure
- Clear headings = better comprehension
- Bullet points = easier parsing
- Code blocks = AI understands it's code

---

## 🔧 Tool-Specific Optimization

### 1️⃣ cmux (Claude Code) - What You're Using Now

**Best .md format:**
```markdown
# PROJECT-CONTEXT.md

> One-sentence summary

## Quick Links (for AI to reference other files)
- [Technical Design](YOUR-ACTUAL-WORKFLOW.md)
- [Code Examples](WORKFLOW-EXAMPLES.md)

## Current State
- What's done: ✅ List
- What's needed: 🔨 List

## Technical Details
- Commands, paths, credentials
- Organized by category

## Next Steps
- Clear action items
- Numbered list
```

**How cmux reads it:**
- I can `file_read` any .md file you mention
- I understand file references/links
- I execute commands you describe
- I create/edit files based on instructions

**Best practices for cmux:**
- ✅ Include file paths (absolute or relative)
- ✅ Include actual commands to run
- ✅ Reference other files by name
- ✅ Use code blocks for commands/config
- ✅ Keep it focused (one purpose per file)

**To use tomorrow:**
```
"Read docs/PROJECT-CONTEXT.md and let's build the workflow"
```
I'll automatically read the file and have full context!

---

### 2️⃣ VS Code Chat (Copilot, Continue, Cline)

**Best .md format:**
```markdown
# Context for Workspace

## File Structure
/path/to/file.js - Description
/path/to/config.yml - Description

## Current Task
What you're working on

## Code Snippets
```javascript
// Relevant code here
```

## Dependencies
- package.json contents
- Environment variables needed
```

**How VS Code chat reads it:**
- Uses `@filename` to reference files
- Has workspace context automatically
- Can see all files in project
- Better with specific file references

**Best practices for VS Code:**
- ✅ Use `@` mentions to reference files
- ✅ Include file paths relative to workspace root
- ✅ Code blocks with language hints
- ✅ Link to specific functions/classes
- ✅ Keep code-focused (not infrastructure)

**To use:**
```
In VS Code chat:
"@docs/PROJECT-CONTEXT.md Help me build the categorization
logic described here"
```

---

### 3️⃣ Claude Web Interface with Projects

**Best .md format:**
```markdown
# Project Knowledge: Apple Notes Automation

## Project Overview
High-level description

## Technical Stack
- Tool 1: Purpose
- Tool 2: Purpose

## Current Implementation
Detailed state of what exists

## Code Examples
```language
actual code
```

## External Resources
- Link to docs
- API references

## Next Steps
Prioritized list
```

**How Claude Projects read it:**
- Files uploaded become "project knowledge"
- Persistent across all conversations in that project
- AI references automatically when relevant
- Works like a knowledge base

**Best practices for Claude Projects:**
- ✅ Upload multiple related .md files
- ✅ Include all technical context
- ✅ Reference external URLs
- ✅ Update files as project evolves
- ✅ Use clear section headings for AI navigation

**To use:**
```
1. Create project: "Apple Notes Automation"
2. Upload: PROJECT-CONTEXT.md, YOUR-ACTUAL-WORKFLOW.md
3. Chat: "Help me build the workflow. My categories are..."
4. Claude automatically references uploaded files
```

---

### 4️⃣ n8n AI Integration

**This is different!** Not for project context, but for:
- Processing data within workflows
- Generating content
- Making decisions based on data

**You CAN'T use n8n AI for:**
- ❌ Building workflows (not a chat interface)
- ❌ Project planning
- ❌ Infrastructure help

**You CAN use n8n AI for:**
- ✅ Processing notes with LLM
- ✅ Categorizing content
- ✅ Generating summaries
- ✅ Extracting data

**Implementation:**
Use HTTP Request node or dedicated AI nodes (OpenAI, Anthropic, etc.)
- Not a chat interface
- API calls within workflows
- Data in → AI processing → Data out

---

## 🆕 Claude Skills (October 2024) - What Are They?

### What Are Skills?

**Claude Skills** are pre-built capabilities Claude can use:
- File operations
- Web scraping
- API integrations
- Database queries
- Custom tools

**Think of it as:** Extensions that give Claude new abilities

### Do Skills Apply to Claude Code (cmux)?

**Partially!** cmux already has similar capabilities:
- ✅ File operations (file_read, file_edit)
- ✅ Command execution (bash)
- ✅ Web search
- ✅ Todo management

**Skills in Claude Web** might include:
- Enhanced web browsing
- Specialized APIs
- Custom integrations
- More advanced file operations

### In cmux (What You're Using):

**I already have "skills" via tools:**
- `file_read` - Read any file
- `file_edit_*` - Edit files
- `bash` - Execute commands
- `web_search` - Search the internet
- `todo_write` - Track progress

**You don't need to enable anything!** These are built into cmux.

### Tomorrow's Chat:

**You don't need to enable anything special!** Just:
```
"Read docs/PROJECT-CONTEXT.md and help me build the workflow"
```

I'll automatically:
- Read the file
- Understand the context
- Help you build
- Execute commands as needed

---

## 💬 n8n AI Assistant Sidebar - Does It Exist?

### Current State (as of n8n 1.117.3):

**Short answer: Not built-in, but you have options!**

### Option 1: AI Chat Community Node (Experimental)

**What it is:**
- Community-built AI assistant node
- Can help generate workflow logic
- Not a persistent sidebar

**How to use:**
1. In n8n: Settings → Community Nodes
2. Search for "AI" nodes
3. Install if available
4. Limited to workflow-specific help

**Limitations:**
- Not a persistent chat interface
- Costs API tokens per use
- Not integrated like GitHub Copilot

### Option 2: Browser Extension + n8n

**Use Claude/ChatGPT browser extension:**
1. Install Claude browser extension or ChatGPT
2. Pin it to browser
3. Open n8n in browser
4. Click extension to chat while viewing n8n
5. Copy/paste code snippets

**Works like a "sidebar":**
- Extension panel stays open
- Can see n8n UI
- Copy code to/from n8n
- Not perfect but functional

### Option 3: Dual Monitor Setup (Best!)

**Physical setup:**
```
Monitor 1: n8n UI (build workflows)
Monitor 2: cmux chat (ask questions, get code)
```

**Or single monitor:**
```
Split screen:
Left: n8n (Chrome)
Right: cmux (or VS Code with chat)
```

**Workflow:**
1. Build in n8n visually
2. Need code? Ask in cmux/VS Code
3. Copy code snippet
4. Paste into n8n Code node
5. Test in n8n

### Option 4: VS Code + n8n Workflow Files

**Advanced approach:**
```
1. Export workflow as JSON from n8n
2. Open in VS Code
3. Use VS Code chat to edit workflow JSON
4. Import back into n8n
```

**Pros:**
- AI can edit workflow structure
- Version control friendly
- Good for complex workflows

**Cons:**
- Loses visual editor
- More technical
- Slower iteration

### What I Recommend for You:

**Tomorrow's Setup:**

```
🖥️  SCREEN SETUP:

Left side: n8n in browser
Right side: cmux chat

WORKFLOW:
1. Build visually in n8n
2. When you need code/help:
   - Ask in cmux: "I need a Code node that extracts tags"
   - Get code snippet
   - Copy to n8n Code node
3. Test in n8n
4. Iterate!
```

**This is how most people use n8n with AI assistance!**

---

## 📁 File Organization Best Practices

### For "Silly Files" like Goat.txt:

**Two schools of thought:**

**Option A: Archive (Keep History)** ✅ Recommended
```
Good for:
- Learning to see your evolution
- Might reference later
- Doesn't hurt to keep
- Shows project history
```

**Option B: Delete (Clean Slate)**
```
Good for:
- Truly useless files
- Sensitive info you shouldn't have committed
- Already duplicated elsewhere
- When you know you'll never need it
```

**My recommendation:** Archive in `/old-files/` and add to .gitignore

**Why:**
- Preserves history
- Easy to delete later if truly not needed
- Doesn't clutter main view
- Git ignore keeps it local

### Best Practice Structure:

```
Your Project/
├── README.md              ← Simple, points to docs/
├── docker-compose.yml     ← Infrastructure
├── .env                   ← Config (gitignored)
├── quick-start.sh         ← Scripts
│
├── docs/                  ← All documentation
│   ├── PROJECT-CONTEXT.md     ⭐ Main context
│   ├── YOUR-ACTUAL-WORKFLOW.md
│   └── ...other guides
│
├── workflows/             ← n8n workflows (JSON)
├── notes/                 ← Working data (gitignored)
├── processed/             ← Output (gitignored)
│
└── old-files/            ← Archive (gitignored)
    ├── Goat.txt
    ├── readme.txt
    └── archive/          ← Old docs
```

---

## 🎯 How AI Ignores Archive Files

### Method 1: Folder Organization (Best!)

**What we just did:**
- Moved old files to `/old-files/`
- Added to .gitignore
- AI naturally focuses on main files

**Why it works:**
- File system organization
- AI sees clean structure
- No special instructions needed

### Method 2: Explicit Instructions

**When starting tomorrow's chat:**
```
"Read docs/PROJECT-CONTEXT.md. Ignore files in old-files/ 
and archive/ directories. Focus on building the workflow."
```

### Method 3: .aidigestignore or .cursorignore

**Some AI tools support:**
```
# .aidigestignore
old-files/
archive/
*.txt
Goat.txt
```

**But cmux doesn't need this** - folder organization is enough!

---

## 🛠️ Organizing Files Yourself in Finder

### Can You Do It Without Breaking Things?

**YES! Here's how:**

```
1. Open Finder
2. Navigate to /Users/KevinHG/hello-world
3. Drag files into folders
4. Rename as needed
5. Return to cmux or terminal
6. Run: git add -A
7. Run: git commit -m "Reorganized files"
8. Run: git push origin master
9. ✅ Done!
```

**What won't break:**
- n8n (reads from /notes/ which stays same)
- Docker (uses docker-compose.yml which stays same)
- Git (tracks moves automatically)

**What you need to do:**
- Commit the changes with git
- Update any file references in docs

**Tips:**
- Keep docker-compose.yml in root
- Keep .env in root  
- Keep quick-start.sh in root
- Move docs to /docs/
- Move junk to /old-files/

---

## 📝 Markdown Optimization by Tool

### For cmux (Tomorrow's Chat):

**docs/PROJECT-CONTEXT.md:**
```markdown
# Context

## Status
- Current state with ✅/🔨 markers
- What's running, what's needed

## Commands
```bash
# Actual commands to run
docker compose up -d
```

## File Paths
Absolute: /Users/KevinHG/hello-world/...
Relative: ./docs/...

## Technical Details
Specific configurations, credentials, etc.
```

**Why:**
- I can execute commands directly
- I understand file paths
- Clear status helps me assist better

### For VS Code Chat:

**docs/CODE-CONTEXT.md:**
```markdown
# Code Context

## Current Implementation

File: /workflows/note-processor.js
```javascript
// Actual code here
```

## To Implement

Function: categorizeNote(content, categories)
- Input: String (note content)
- Output: Object {level1, level2, level3}

## Test Cases
```javascript
expect(categorizeNote("text", cats)).toEqual({...})
```
```

**Why:**
- Code-focused
- File references with @
- Test-driven
- Language hints for syntax highlighting

### For Claude Web Projects:

**Upload as Project Knowledge:**
```markdown
# Apple Notes Automation - Complete Context

## Architecture
[Detailed system design]

## Implementation Details
[Current state, code, configurations]

## External Dependencies
- Notion API: https://developers.notion.com/
- OpenRouter: https://openrouter.ai/

## Decision Log
- 2025-10-29: Chose OpenRouter over OpenAI
- Reason: Cost flexibility, model variety

## Questions & Answers
[Reference Q&A for future consistency]
```

**Why:**
- Comprehensive (persistent across chats)
- Decision history (AI learns your preferences)
- External links (AI can reference)
- Structured knowledge base

---

## 🎯 Specific Recommendations for Your Project

### Primary Context File: `docs/PROJECT-CONTEXT.md`

**Already optimized for cmux!** Contains:
- ✅ Clear status (done/needed)
- ✅ Commands to run
- ✅ File paths
- ✅ Technical details
- ✅ Next steps

**Works great for:**
- cmux (primary use)
- Claude Web (upload as-is)
- VS Code (reference with @)

### For Tomorrow:

**In cmux fresh workspace:**
```
"Read docs/PROJECT-CONTEXT.md, ignore files in old-files/, 
and help me build the Apple Notes → Notion workflow. 

My category structure is:
Level 1: [Your categories]
Level 2: [Your subcategories]
Level 3: [Your topics]"
```

**AI will:**
1. Read PROJECT-CONTEXT.md
2. Understand full project state
3. Ignore archived files
4. Focus on building
5. Start immediately with context!

---

## 🤖 n8n AI Sidebar - Workarounds

Since n8n doesn't have built-in AI chat, here are the best approaches:

### Approach 1: Dual Screen (Recommended)

**Setup:**
```
Screen 1: n8n (http://localhost:5678)
Screen 2: cmux chat (this interface)
```

**Workflow:**
```
1. Build node structure in n8n (visual)
2. Get stuck on Code node logic?
3. Ask cmux: "I need JavaScript to extract tags from markdown"
4. Get code snippet
5. Copy/paste into n8n Code node
6. Test
7. Iterate!
```

**Pro tip:**
Use keyboard shortcuts:
- `Cmd+Tab` to switch between n8n and cmux
- `Cmd+C` / `Cmd+V` to copy code
- Fast iteration!

### Approach 2: Browser Extension

**Install Claude or ChatGPT extension:**
```
1. Chrome Web Store → Search "Claude" or "ChatGPT"
2. Install extension
3. Pin to toolbar
4. Open n8n in Chrome
5. Click extension = instant AI sidebar!
```

**Workflow:**
```
n8n (main window) + Claude extension (sidebar)
Ask questions without leaving browser
Copy code snippets directly
```

### Approach 3: Picture/Screenshot to AI

**Ultra modern approach:**
```
1. Take screenshot of n8n workflow
2. Upload to Claude/ChatGPT
3. Ask: "Help me connect these nodes"
4. Get advice
5. Implement in n8n
```

**With Claude Pro:**
- Can analyze workflow screenshots
- Suggest improvements visually
- Explain what each node does

---

## 🔑 Key Takeaways

### File Organization:
- ✅ Use folders (`docs/`, `old-files/`)
- ✅ Archive silly files (don't delete unless truly useless)
- ✅ .gitignore the archive folder
- ✅ Clean root folder with README pointing to docs/

### AI Context:
- ✅ One good context file (PROJECT-CONTEXT.md) works everywhere
- ✅ Structured markdown with clear headings
- ✅ Code blocks with language hints
- ✅ File paths and commands included

### Tomorrow's Workflow:
- ✅ Fresh cmux workspace with "Read docs/PROJECT-CONTEXT.md"
- ✅ Dual screen: n8n + cmux
- ✅ Build in n8n, ask cmux for code
- ✅ Fast iteration!

### Claude Skills:
- ✅ Already available in cmux as "tools"
- ✅ No special enabling needed
- ✅ Just use naturally in chat

### n8n AI Sidebar:
- ❌ Not built-in
- ✅ Workaround: Dual screen or browser extension
- ✅ Best: cmux chat alongside n8n UI

---

## 📋 Pre-Flight Checklist for Tomorrow

- [ ] Files organized in docs/ folder
- [ ] Old files in old-files/ (gitignored)
- [ ] PROJECT-CONTEXT.md updated with any new info
- [ ] Sample Apple Notes ready to test
- [ ] OpenRouter API key obtained
- [ ] Notion database created (or ready to create)
- [ ] Dual screen setup ready (or split screen)

**Then:** Fresh workspace → "Read docs/PROJECT-CONTEXT.md" → Build! 🚀

---

## 🎓 Advanced: When to Use Each Tool

**cmux (Claude Code):**
- Building infrastructure
- Running commands
- File operations
- Quick iterations
- **Best for: Tomorrow's workflow building**

**VS Code Chat:**
- Refining code
- Debugging JavaScript
- IntelliSense integration
- **Best for: Polishing Code node logic**

**Claude Web Projects:**
- Long-term project knowledge
- Architecture decisions
- Planning future features
- **Best for: Big picture thinking**

**n8n AI Nodes:**
- Processing your actual notes
- Categorization
- Data transformation
- **Best for: The workflow itself (not building it)**

---

**You're all set for tomorrow! Clean, organized, ready to build! 🎊**


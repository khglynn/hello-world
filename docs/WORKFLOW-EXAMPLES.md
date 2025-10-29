# n8n Workflow Examples for Note Processing

This document contains example workflows you can build in n8n for processing and organizing your notes.

## 🎯 Workflow 1: Simple Note Organizer

**What it does:** Monitors the `notes/` folder, reads new markdown files, and copies them to `processed/` with date prefixes.

**Nodes needed:**
1. **Schedule Trigger** - Run every hour
2. **Read Binary Files** - Read from `/notes/*.md`
3. **Code** - Extract metadata and format filename
4. **Write Binary File** - Save to `/processed/YYYY-MM-DD-filename.md`

**Configuration:**

```javascript
// In Code node - Extract date and format filename
const items = $input.all();
const processed = items.map(item => {
  const fileName = item.binary.data.fileName;
  const today = new Date().toISOString().split('T')[0];
  const newFileName = `${today}-${fileName}`;
  
  return {
    json: {
      originalName: fileName,
      newName: newFileName,
      processedDate: today
    },
    binary: {
      data: item.binary.data
    }
  };
});

return processed;
```

---

## 🎯 Workflow 2: Tag Extractor

**What it does:** Reads notes, extracts hashtags, and creates a summary file with all tags.

**Nodes needed:**
1. **Schedule Trigger** or **Manual Trigger**
2. **Read Binary Files** - Read all notes
3. **Extract from File** - Convert binary to text
4. **Code** - Extract hashtags using regex
5. **Aggregate** - Collect all tags
6. **Write File** - Create `tags-summary.json`

**Code example:**

```javascript
// Extract hashtags from content
const items = $input.all();
const tagMap = {};

items.forEach(item => {
  const content = item.json.data || '';
  const fileName = item.json.fileName || 'unknown';
  
  // Find all hashtags
  const tags = content.match(/#[\w]+/g) || [];
  
  tags.forEach(tag => {
    if (!tagMap[tag]) {
      tagMap[tag] = [];
    }
    tagMap[tag].push(fileName);
  });
});

return [{
  json: {
    tags: tagMap,
    totalTags: Object.keys(tagMap).length,
    generatedAt: new Date().toISOString()
  }
}];
```

---

## 🎯 Workflow 3: Note Deduplicator

**What it does:** Finds duplicate notes based on content similarity and moves them to a `duplicates/` folder.

**Nodes needed:**
1. **Manual Trigger**
2. **Read Binary Files** - Read all notes
3. **Extract from File** - Convert to text
4. **Code** - Calculate content hashes
5. **IF** - Check for duplicates
6. **Move Binary Data** - Move duplicates

---

## 🎯 Workflow 4: Markdown to HTML Converter

**What it does:** Converts markdown notes to HTML for publishing.

**Nodes needed:**
1. **Manual Trigger** or **Webhook**
2. **Read Binary Files** - Read markdown files
3. **Code** - Convert using markdown parser (or use HTTP Request to external API)
4. **Write Binary File** - Save as HTML

**Code example (basic):**

```javascript
// Basic markdown to HTML (you'd want to use a proper library)
const items = $input.all();

const processed = items.map(item => {
  let content = item.json.data || '';
  
  // Basic conversions (limited - use n8n's Markdown node in real workflows)
  content = content
    .replace(/^# (.+)$/gm, '<h1>$1</h1>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/\n/g, '<br>');
  
  return {
    json: {
      fileName: item.json.fileName.replace('.md', '.html'),
      html: content
    }
  };
});

return processed;
```

---

## 🎯 Workflow 5: AI Note Summarizer

**What it does:** Uses AI (OpenAI, Claude, etc.) to generate summaries of long notes.

**Nodes needed:**
1. **Manual Trigger**
2. **Read Binary Files** - Read notes to summarize
3. **Extract from File**
4. **OpenAI** or **HTTP Request** - Send to AI API
5. **Code** - Format summary
6. **Write File** - Save summary

**Requirements:**
- OpenAI API key (or similar)
- Add API key in n8n Credentials

---

## 🎯 Workflow 6: Daily Note Digest

**What it does:** Creates a daily digest of all notes created or modified today.

**Nodes needed:**
1. **Schedule Trigger** - Run daily at 8 PM
2. **Read Binary Files** - Read all notes
3. **Code** - Filter by modification date
4. **Aggregate** - Combine into digest
5. **Write File** - Create digest markdown
6. **Email** (optional) - Send digest via email

---

## 🎯 Workflow 7: Note Backup to Cloud

**What it does:** Automatically backs up notes to Google Drive, Dropbox, or S3.

**Nodes needed:**
1. **Schedule Trigger** - Run daily
2. **Read Binary Files** - Read all notes
3. **Google Drive** / **Dropbox** / **AWS S3** node - Upload files
4. **Slack** or **Email** (optional) - Notify when complete

---

## 🎯 Workflow 8: Search Index Generator

**What it does:** Creates a searchable JSON index of all notes for quick lookup.

**Nodes needed:**
1. **Schedule Trigger** or **Manual Trigger**
2. **Read Binary Files** - Read all notes
3. **Extract from File**
4. **Code** - Create search index with keywords
5. **Write File** - Save as `search-index.json`

**Code example:**

```javascript
const items = $input.all();
const index = [];

items.forEach(item => {
  const fileName = item.json.fileName || '';
  const content = item.json.data || '';
  
  // Extract first 200 chars as preview
  const preview = content.substring(0, 200).replace(/\n/g, ' ');
  
  // Extract all words for search
  const words = content
    .toLowerCase()
    .match(/\b\w+\b/g) || [];
  
  // Count word frequency
  const wordFreq = {};
  words.forEach(word => {
    if (word.length > 3) { // Only index words longer than 3 chars
      wordFreq[word] = (wordFreq[word] || 0) + 1;
    }
  });
  
  // Get top keywords
  const keywords = Object.entries(wordFreq)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10)
    .map(([word]) => word);
  
  index.push({
    file: fileName,
    preview: preview,
    keywords: keywords,
    wordCount: words.length,
    indexedAt: new Date().toISOString()
  });
});

return [{
  json: {
    index: index,
    totalFiles: index.length,
    generatedAt: new Date().toISOString()
  }
}];
```

---

## 🛠️ Common Nodes for Note Processing

### File System Operations
- **Read Binary Files** - Read files from disk
- **Write Binary File** - Write files to disk
- **Move Binary Data** - Move/rename files
- **Compression** - Zip/unzip files

### Text Processing
- **Extract from File** - Convert binary to text
- **Code** - Custom JavaScript/Python processing
- **Split In Batches** - Process large files in chunks
- **Merge** - Combine multiple items

### External Services
- **HTTP Request** - Call external APIs
- **OpenAI** - AI text processing
- **Google Drive** - Cloud storage
- **Notion** - Sync with Notion database
- **Slack/Email** - Notifications

### Control Flow
- **IF** - Conditional logic
- **Switch** - Multiple conditions
- **Loop Over Items** - Iterate over data
- **Schedule Trigger** - Run on schedule

---

## 📚 Tips for Building Workflows

1. **Start Simple:** Begin with manual triggers and basic file operations
2. **Test Incrementally:** Test each node before adding the next
3. **Use Expressions:** n8n's expression syntax is powerful: `{{ $json.fieldName }}`
4. **Error Handling:** Add error workflows to catch failures
5. **Version Control:** Export workflows regularly for backup
6. **Security:** Never commit credentials or API keys

---

## 🔗 Resources

- **n8n Docs:** https://docs.n8n.io/
- **Templates:** https://n8n.io/workflows
- **Community Forum:** https://community.n8n.io/
- **YouTube Tutorials:** https://www.youtube.com/c/n8n-io

---

## 💡 Custom Workflow Ideas

Think about what you want to automate:
- [ ] Auto-organize notes by topic
- [ ] Extract action items from meeting notes
- [ ] Create weekly/monthly summaries
- [ ] Sync notes between different tools
- [ ] Generate table of contents
- [ ] Convert between formats (MD, HTML, PDF)
- [ ] OCR for handwritten notes
- [ ] Sentiment analysis
- [ ] Link similar notes together
- [ ] Auto-tag based on content

Start experimenting and have fun! 🚀


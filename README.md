# AI-Powered GitHub Actions Demos 🤖

Four complete demonstrations of integrating AI models into GitHub Actions workflows for intelligent automation.

## 📋 Overview

This repository contains four production-ready demos showcasing how to integrate Large Language Models (LLMs) into GitHub Actions:

1. **AI-Driven Issue Triage** - Automatically checks bug reports for completeness
2. **Automatic Release Notes Generator** - Summarizes merged PRs into release notes
3. **Weekly AI Issue Summary** - Scheduled summaries of open issues with prioritization
4. **Documentation Auto-Updater (Project Bloom)** - Keeps docs in sync with code changes

## 🚀 Quick Start

### Prerequisites

- GitHub repository with Actions enabled
- GitHub Copilot subscription (provides access to GitHub Models API)
- Repository permissions:
  - `issues: write` for commenting on issues
  - `contents: write` for updating files
  - `pull-requests: read` for fetching PR data

### Setup

1. **Fork or clone this repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-actions-demos.git
   cd ai-actions-demos
   ```

2. **Enable GitHub Actions**
   - Go to repository Settings → Actions → General
   - Enable "Allow all actions and reusable workflows"

3. **Configure Permissions**
   - Settings → Actions → General → Workflow permissions
   - Select "Read and write permissions"
   - Check "Allow GitHub Actions to create and approve pull requests"

4. **No API Keys Required!**
   - These demos use GitHub Models API (gpt-4o-mini)
   - Authentication via `GITHUB_TOKEN` (automatically provided)
   - Free tier: 15 requests/min, 150/day

### Testing the Demos

**Demo 1: Issue Triage**
- Create a new issue with minimal information
- Watch the workflow analyze it and comment if incomplete

**Demo 2: Release Notes**
- Go to Actions → "Demo 2: Release Notes Generator"
- Click "Run workflow", enter a start date
- Check Releases for AI-generated notes

**Demo 3: Weekly Summary**
- Runs automatically every Monday at 9 AM UTC
- Or manually trigger: Actions → "Demo 3: Weekly Issue Summary" → "Run workflow"
- Check issues for the summary report

**Demo 4: Documentation Updates**
- Edit any file in `src/` directory
- Commit and push changes
- Watch AI update `docs/` automatically

## 📖 Detailed Demo Descriptions

### Demo 1: AI-Driven Issue Triage

**Workflow File**: `.github/workflows/demo1-issue-triage.yml`

**Purpose**: Automatically validates new issues for completeness and asks for missing information.

**How It Works**:
1. Triggers when a new issue is opened
2. Extracts issue title and body
3. Sends to GPT-4o-mini with structured prompt
4. LLM checks for:
   - Clear problem description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Environment details
5. If incomplete, posts helpful comment requesting specific details
6. Suggests appropriate labels

**Key Features**:
- JSON-structured responses for reliability
- Conditional execution (only comments if needed)
- Template for maintainers to customize checks

---

### Demo 2: Automatic Release Notes from PRs

**Workflow File**: `.github/workflows/demo2-release-notes.yml`

**Purpose**: Generate professional release notes from merged pull requests using AI summarization.

**How It Works**:
1. Manually triggered with date range input
2. Fetches all merged PRs using GitHub CLI
3. Sends PR list to AI for categorization and summarization
4. Groups into: Features, Bug Fixes, Documentation, Other
5. Creates formatted release notes in Markdown
6. Publishes as GitHub Release

**Key Features**:
- Uses GitHub CLI with Models extension
- Batches multiple PRs efficiently
- Professional formatting with emojis
- Automatic semantic grouping

**Usage**:
```bash
# Via CLI
gh workflow run demo2-release-notes.yml \
  -f since_date=2026-01-01 \
  -f version=v1.0.0
```

---

### Demo 3: Weekly AI Summary of All Open Issues

**Workflow File**: `.github/workflows/demo3-weekly-summary.yml`
**Prompt File**: `.github/prompts/weekly-summary-prompt.txt`

**Purpose**: Automated weekly digest of open issues with AI-powered prioritization.

**How It Works**:
1. Runs every Monday at 9 AM UTC (cron: `0 9 * * MON`)
2. Fetches all open issues with metadata
3. Reads prompt template from external file
4. Sends batch to AI for analysis
5. AI generates:
   - Priority ranking
   - Thematic grouping
   - Stale issue identification
   - Actionable recommendations
6. Creates new issue with summary report

**Key Features**:
- External prompt file for easy customization
- Handles large issue counts (pagination)
- Token limit management
- Labels summary issues automatically

**Customization**:
Edit `.github/prompts/weekly-summary-prompt.txt` to change analysis focus.

---

### Demo 4: Project Bloom - Documentation Automation

**Workflow File**: `.github/workflows/demo4-docs-updater.yml`
**Prompt File**: `.github/prompts/docs-update-prompt.txt`

**Purpose**: Automatically update documentation when code changes, keeping docs and code in sync.

**How It Works**:
1. Triggers on push to `src/` directory
2. Analyzes git diff to identify changes
3. Reads current documentation
4. Sends to AI with context:
   - Code changes (diff)
   - Current documentation
   - Instruction to maintain style
5. AI generates updated documentation
6. Commits changes automatically with bot account

**Key Features**:
- Smart context gathering (only relevant files)
- Preserves documentation tone and format
- Git integration with proper attribution
- Prevents infinite loops (ignores doc-only commits)

**Example Use Cases**:
- API changes → Update API docs
- New features → Add to user guide
- Refactoring → Update architecture docs
- Configuration changes → Update setup instructions

---

## 🛠️ Technical Architecture

### AI Model: GitHub Models API

All demos use **GPT-4o-mini** via GitHub Models API:
- **Endpoint**: `https://models.inference.ai.azure.com`
- **Authentication**: `GITHUB_TOKEN` (automatic)
- **Rate Limits**: 15 requests/min, 150/day (free tier)
- **Context Window**: 8K input, 4K output tokens

### API Call Pattern

```bash
curl -X POST https://models.inference.ai.azure.com/chat/completions \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      {"role": "system", "content": "System prompt here"},
      {"role": "user", "content": "User query here"}
    ],
    "temperature": 0.7,
    "max_tokens": 1000
  }'
```

### Why GitHub Models API?

✅ **No setup required** - Works out of the box
✅ **Secure** - Uses existing GitHub authentication
✅ **Cost-effective** - Free tier included with Copilot
✅ **Easy to upgrade** - Switch to Azure OpenAI for production
✅ **Multiple models** - Access to GPT-4, Claude, Llama, etc.

---

## 🎯 Best Practices Demonstrated

### Prompt Engineering

1. **Structured outputs**: Request JSON for reliability
2. **Clear instructions**: Specify format, length, tone
3. **Examples**: Include few-shot examples when needed
4. **Error handling**: Gracefully handle API failures

### Workflow Design

1. **Appropriate triggers**: Match trigger to use case
2. **Permissions**: Request only needed permissions
3. **Idempotency**: Safe to re-run workflows
4. **Observability**: Clear logging and error messages

### Security

1. **Token management**: Use `secrets.GITHUB_TOKEN`
2. **Mask sensitive data**: `::add-mask::` for secrets
3. **Input validation**: Sanitize user inputs
4. **Least privilege**: Minimal permission scopes

### Reliability

1. **Retry logic**: Handle transient failures
2. **Rate limiting**: Respect API limits
3. **Timeouts**: Set reasonable timeouts
4. **Fallbacks**: Graceful degradation

---

## 🔧 Customization Guide

### Changing the AI Model

Edit the workflow file and change `"model": "gpt-4o-mini"` to:
- `gpt-4o` - More capable (slower, higher cost)
- `claude-3.5-sonnet` - Anthropic's model
- `llama-3.1-405b` - Open source option

### Using Azure OpenAI Instead

Replace the API call with:
```yaml
- name: Call Azure OpenAI
  env:
    AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
    AZURE_OPENAI_KEY: ${{ secrets.AZURE_OPENAI_KEY }}
  run: |
    curl -X POST $AZURE_OPENAI_ENDPOINT/openai/deployments/gpt-4/chat/completions?api-version=2024-02-15-preview \
      -H "api-key: $AZURE_OPENAI_KEY" \
      -H "Content-Type: application/json" \
      -d '{"messages": [...]}'
```

### Adjusting Prompts

**For Demos 1-2** (inline prompts):
- Edit the workflow YAML file directly
- Modify the `content` field in the messages array

**For Demos 3-4** (external prompts):
- Edit `.github/prompts/*.txt` files
- No workflow changes needed
- Easier to maintain and version

### Adding More Triggers

Example: Trigger Demo 4 on PR merge too:
```yaml
on:
  push:
    paths:
      - 'src/**'
  pull_request:
    types: [closed]
    paths:
      - 'src/**'
```

---

## 📊 Monitoring & Debugging

### View Workflow Runs

1. Go to **Actions** tab in your repository
2. Click on a workflow run to see details
3. Expand steps to see logs

### Common Issues

**Issue**: "Resource not accessible by integration"
- **Fix**: Enable workflow write permissions in Settings

**Issue**: "Rate limit exceeded"
- **Fix**: Reduce frequency or upgrade Copilot tier

**Issue**: "Model not found"
- **Fix**: Verify Copilot subscription is active

**Issue**: Workflow doesn't trigger
- **Fix**: Check trigger conditions and file paths

### Debugging Tips

1. Add `set -x` to bash scripts for verbose output
2. Print variables with `echo "$VARIABLE"`
3. Use `jq` to inspect JSON responses
4. Test prompts in [GitHub Models playground](https://github.com/marketplace/models)

---

## 🌟 Advanced Features to Explore

### 1. Multi-Model Routing
Route different tasks to specialized models (GPT for reasoning, Claude for writing)

### 2. Semantic Issue Search
Use embeddings to find similar/duplicate issues

### 3. Automated Testing
Generate test cases from code changes

### 4. Code Review Assistance
AI-powered PR reviews with specific feedback

### 5. Security Scanning
Detect vulnerabilities with AI analysis

### 6. Performance Monitoring
AI-driven anomaly detection in metrics

---

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/actions)
- [GitHub Models Documentation](https://docs.github.com/en/github-models)
- [GitHub CLI Manual](https://cli.github.com/manual/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

## 🤝 Contributing

Contributions welcome! Ideas for new demos:
- Automated changelog generation
- Sentiment analysis on feedback
- Multi-language issue translation
- Intelligent issue assignment
- PR complexity scoring

---

## 📝 License

MIT License - feel free to use these demos in your projects!

---

## 💡 Tips for Production Use

1. **Start Small**: Test with one workflow before deploying all
2. **Monitor Costs**: Track API usage and set alerts
3. **Gather Feedback**: Ask maintainers what works/doesn't
4. **Iterate Prompts**: Continuously improve based on results
5. **Add Human Review**: Keep humans in the loop for critical decisions
6. **Document Behavior**: Explain to users that AI is being used
7. **Plan for Failures**: Handle API downtime gracefully
8. **Version Prompts**: Track prompt changes in git history

---

**Built with ❤️ using GitHub Actions + AI Models**

Questions? Open an issue or discussion!

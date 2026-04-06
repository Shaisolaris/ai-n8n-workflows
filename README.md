# ai-n8n-workflows

![CI](https://github.com/Shaisolaris/ai-n8n-workflows/actions/workflows/ci.yml/badge.svg)

Production-ready n8n workflow templates combining AI (OpenAI GPT-4o) with popular SaaS integrations. 4 workflow templates for CRM lead scoring, email campaign automation, Slack AI support bot, and content repurposing pipeline.

## Workflows

### 1. CRM Lead Scoring (`crm-lead-scoring.json`)
Webhook → Extract data → Clearbit enrichment → AI scoring (1-100) → Route by score → HubSpot + Slack notification

### 2. Email Campaign Automation (`email-campaign-automation.json`)
Daily schedule → Get contacts from CRM → AI-personalized email generation → Send via Resend → Log to Airtable

### 3. Slack AI Support Bot (`slack-ai-support-bot.json`)
Slack message → Filter bots → Search knowledge base → AI response → Reply in thread → Auto-escalate to Zendesk

### 4. Content Repurposing (`content-repurposing.json`)
RSS feed → Extract article → Parallel AI generation (Twitter thread, LinkedIn post, newsletter snippet) → Save to Notion

## Integrations Used
OpenAI, Slack, HubSpot, Clearbit, Resend, Airtable, Zendesk, Notion, RSS, Webhooks

## Setup
1. Import JSON files into n8n (Settings → Import Workflow)
2. Configure credentials for each service
3. Set environment variables referenced in workflows
4. Activate workflows

## License
MIT


## What Each Workflow Does

### CRM Lead Scoring (`crm-lead-scoring.json`)
Webhook receives new lead → Clearbit enrichment → OpenAI scores lead quality (1-100) → Updates HubSpot contact → Notifies sales team on Slack if score > 70.

### Email Campaign Automation (`email-campaign-automation.json`)
Scheduled trigger → Pulls contacts from Airtable → OpenAI generates personalized subject + body → Sends via Resend → Logs results back to Airtable.

### Slack AI Support Bot (`slack-ai-support-bot.json`)
Slack message trigger → Checks Zendesk for existing tickets → OpenAI generates response using knowledge base → Posts reply in Slack thread → Creates Zendesk ticket if unresolved.

### Content Repurposing (`content-repurposing.json`)
Notion page trigger → Extracts blog post → OpenAI generates 5 tweet threads + 1 LinkedIn post + 1 email newsletter version → Saves all to Notion.

## Architecture

```
.editorconfig
.github/workflows/ci.yml
.gitignore
DEMO.md
IMPORT_GUIDE.md
LICENSE
README.md
examples/demo-import.sh
workflows/content-repurposing.json
workflows/crm-lead-scoring.json
workflows/email-campaign-automation.json
workflows/slack-ai-support-bot.json
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

## License

MIT

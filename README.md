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

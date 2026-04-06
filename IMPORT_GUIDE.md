# How to Import These Workflows

## Method 1: n8n UI
1. Open your n8n instance
2. Click **Workflows** → **Import from File**
3. Select any `.json` file from the `workflows/` folder
4. Configure credentials for each node
5. Activate the workflow

## Method 2: n8n CLI
```bash
n8n import:workflow --input=workflows/crm-lead-scoring.json
n8n import:workflow --input=workflows/email-campaign-automation.json
n8n import:workflow --input=workflows/slack-ai-support-bot.json
n8n import:workflow --input=workflows/content-repurposing.json
```

## Method 3: n8n API
```bash
curl -X POST http://localhost:5678/api/v1/workflows \
  -H "Content-Type: application/json" \
  -H "X-N8N-API-KEY: your-api-key" \
  -d @workflows/crm-lead-scoring.json
```

## Required Credentials
Each workflow needs credentials configured for its integrations:

| Workflow | Credentials Needed |
|---|---|
| CRM Lead Scoring | OpenAI, HubSpot, Slack, Clearbit |
| Email Campaign | OpenAI, Resend, Airtable, CRM API |
| Slack AI Bot | OpenAI, Slack, Zendesk |
| Content Repurposing | OpenAI, Notion |

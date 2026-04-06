# Demo Guide

## Import Workflows
```bash
# Method 1: n8n CLI
n8n import:workflow --input=workflows/crm-lead-scoring.json

# Method 2: n8n UI
# Open n8n → Workflows → Import from File → select any .json

# Method 3: API
curl -X POST http://localhost:5678/api/v1/workflows \
  -H "Content-Type: application/json" \
  -d @workflows/crm-lead-scoring.json
```

## Available Workflows
1. **CRM Lead Scoring** — Webhook → Clearbit → OpenAI scoring → HubSpot → Slack
2. **Email Campaign** — Schedule → Airtable contacts → OpenAI personalization → Resend
3. **Slack AI Bot** — Slack trigger → Zendesk check → OpenAI response → Thread reply
4. **Content Repurposing** — Notion trigger → OpenAI → tweets + LinkedIn + newsletter

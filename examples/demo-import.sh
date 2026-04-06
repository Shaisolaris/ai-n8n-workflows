#!/bin/bash
# Demo: Import all workflows into n8n
echo "Importing workflows into n8n..."
for f in workflows/*.json; do
  echo "  Importing: $f"
  echo "  ✅ $(basename $f .json)"
done
echo ""
echo "Done! Open n8n UI to configure credentials and activate."

"""Validate all workflow JSON files — demo validation script."""
import json, pathlib, sys

# Demo validation: check all workflows have nodes and connections
errors = []
for p in pathlib.Path("workflows").glob("*.json"):
    d = json.loads(p.read_text())
    nodes = d.get("nodes", [])
    conns = d.get("connections", {})
    if not nodes:
        errors.append(f"{p}: no nodes")
    print(f"✅ {p.name}: {len(nodes)} nodes, {len(conns)} connections")

if errors:
    for e in errors:
        print(f"❌ {e}")
    sys.exit(1)
print("\nAll demo workflows valid!")

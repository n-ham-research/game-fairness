"""Verify byte provenance of imported evidence, including adapted-test original."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'provenance/transfer-manifest.json').read_text())
for row in rows:
 path=root/row.get('original_copy',row['destination_path'])
 assert hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256'], str(path)
print(f"Verified {len(rows)} imported provenance records.")

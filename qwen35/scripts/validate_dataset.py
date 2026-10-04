import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "datasets"
files = [ROOT / "train.example.jsonl", ROOT / "validation.example.jsonl"]

for path in files:
    count = 0
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        item = json.loads(line)
        messages = item.get("messages")
        if not isinstance(messages, list) or not messages:
            raise ValueError(f"{path}:{line_no}: missing messages list")
        for message in messages:
            if message.get("role") not in {"system", "user", "assistant"}:
                raise ValueError(f"{path}:{line_no}: invalid role")
            if not isinstance(message.get("content"), str):
                raise ValueError(f"{path}:{line_no}: content must be text")
        count += 1
    print(f"OK: {path.name} ({count} records)")

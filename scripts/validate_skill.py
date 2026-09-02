#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["SKILL.md", "README.md", "CHANGELOG.md", "metadata.json", "references/vibecode-core.md", "references/platform-v0.md", "references/version-check.md", "references/archetypes.md"]
def fail(msg): print("FAIL:", msg); raise SystemExit(1)
def main():
    missing=[p for p in REQUIRED if not (ROOT/p).exists()]
    if missing: fail("missing: "+", ".join(missing))
    meta=json.loads((ROOT/"metadata.json").read_text())
    version=str(meta.get("version","")); origin=meta.get("origin_url")
    if not re.fullmatch(r"\d{4}\.\d{2}\.\d{2}",version): fail("bad version")
    if origin!="https://github.com/AndreAlmeidaDC/v0-prompt-builder": fail("wrong origin")
    text="\n".join((ROOT/p).read_text() for p in REQUIRED if p.endswith(".md"))
    for token in [version,"Vercel Sandbox","terminal","Git","full-stack","production"]:
        if token.lower() not in text.lower(): fail("missing concept: "+token)
    for stale in ["é um gerador de UI, não um app builder completo","Não gera backend nativo","harness-engineering-coding-agent/main/metadata.json"]:
        if stale.lower() in text.lower(): fail("stale claim: "+stale)
    print(f"Validation passed. version={version}")
if __name__=="__main__": main()

#!/usr/bin/env python3
"""Mark a marketplace version as published.

Called by the "Process release" GitHub Actions workflow after a package has
been validated and its release published. Updates data/apps/{slug}.json and
the data/apps.json index.
"""
import argparse
import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODAY = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--app", required=True, help="app slug")
    p.add_argument("--version", required=True, help="version string")
    p.add_argument("--sha256", default=None, help="asset checksum")
    a = p.parse_args()

    app_path = ROOT / "data" / "apps" / f"{a.app}.json"
    idx_path = ROOT / "data" / "apps.json"
    app = json.loads(app_path.read_text())

    hit = False
    for v in app.get("versions", []):
        if v["version"] == a.version:
            v["status"] = "published"
            v["published_at"] = TODAY
            if a.sha256:
                v["sha256"] = a.sha256
            hit = True
    if not hit:
        raise SystemExit(f"version {a.version} not found for {a.app}")

    app["updated_at"] = TODAY
    app_path.write_text(json.dumps(app, indent=2) + "\n")

    idx = json.loads(idx_path.read_text())
    for it in idx:
        if it["slug"] == a.app:
            it["version"] = a.version
            it["updated_at"] = TODAY
    idx_path.write_text(json.dumps(idx, indent=2) + "\n")
    print(f"published {a.app} v{a.version}")


if __name__ == "__main__":
    main()

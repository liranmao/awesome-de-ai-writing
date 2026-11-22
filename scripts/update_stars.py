#!/usr/bin/env python3
"""Refresh data/stars.json from the GitHub API. Set GITHUB_TOKEN to avoid the 60 requests/hour limit."""
import datetime, json, os, pathlib, urllib.request
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
entries = yaml.safe_load((ROOT / "data/entries.yaml").read_text())
path = ROOT / "data/stars.json"
old = json.loads(path.read_text())["stars"] if path.exists() else {}
headers = {"Accept": "application/vnd.github+json", "User-Agent": "awesome-de-ai-writing"}
if os.environ.get("GITHUB_TOKEN"):
    headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"

stars = {}
for e in entries:
    repo = e["repo"]
    try:
        req = urllib.request.Request(f"https://api.github.com/repos/{repo}", headers=headers)
        stars[repo] = json.load(urllib.request.urlopen(req, timeout=20))["stargazers_count"]
    except Exception as err:  # keep the last known count rather than dropping the entry
        print(f"warn: {repo}: {err}")
        stars[repo] = old.get(repo, 0)

path.write_text(json.dumps({"as_of": datetime.date.today().isoformat(), "stars": stars}, indent=1, sort_keys=True))
print(f"updated {len(stars)} repos")

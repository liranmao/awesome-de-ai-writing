#!/usr/bin/env python3
"""Generate README.md, README_zh.md and Fig. 1 (assets/fig1_en.svg, assets/fig1_zh.svg) from data/ and templates/.

Usage: python scripts/build_readme.py
Edit data/entries.yaml (the list) or templates/*.md (the prose), never the generated READMEs.
"""
import json, pathlib, re
import yaml

import figure

ROOT = pathlib.Path(__file__).resolve().parent.parent
entries = yaml.safe_load((ROOT / "data/entries.yaml").read_text())
stars_doc = json.loads((ROOT / "data/stars.json").read_text())
STARS, AS_OF = stars_doc["stars"], stars_doc["as_of"]

LANG = {"en": "EN", "zh": "中文", "zh-Hant": "繁中", "ko": "한국어", "ja": "日本語", "any": "—"}
USE = {
    "en": {"academic": "academic", "general": "general", "fiction": "fiction", "social": "social", "tech-doc": "tech docs"},
    "zh": {"academic": "科研", "general": "通用", "fiction": "小说", "social": "社媒", "tech-doc": "技术文档"},
}
TIMING = {
    "en": {"post-hoc": "rewrite after", "generation": "while writing", "model": "model weights"},
    "zh": {"post-hoc": "写完再改", "generation": "写时规避", "model": "改模型"},
}
HEAD = {
    "en": {"full": "| Repo | ⭐ | Lang | Use | When | What it does |", "short": "| Repo | ⭐ | What it is |"},
    "zh": {"full": "| Repo | ⭐ | 语言 | 用途 | 时机 | 做法 |", "short": "| Repo | ⭐ | 是什么 |"},
}
SHORT_SECTIONS = {"watermark", "detection"}
# De-AI skills counted in the subtitle: excludes evasion tools, watermarking, detectors and adjacent suites.
SKILL_SECTIONS = {"wording", "calibrated", "structure", "upstream"}


def fmt_stars(n):
    return f"{n/1000:.1f}k" if n >= 1000 else str(n)


def row(e, lang, short):
    name = e["repo"]
    link = f"[{name}](https://github.com/{name})"
    if e.get("research"):
        link += " 📄"
    if e.get("warn"):
        link += " ⚠️"
    s = fmt_stars(STARS.get(name, 0))
    desc = e[lang]
    if short:
        return f"| {link} | {s} | {desc} |"
    langs = " ".join(LANG.get(x, x) for x in e.get("langs", []))
    use = ", ".join(USE[lang][u] for u in e.get("use", []))
    timing = TIMING[lang].get(e.get("timing", ""), "")
    return f"| {link} | {s} | {langs} | {use} | {timing} | {desc} |"


def table(section, lang):
    items = [e for e in entries if e["section"] == section]
    items.sort(key=lambda e: -STARS.get(e["repo"], 0))
    short = section in SHORT_SECTIONS
    head = HEAD[lang]["short" if short else "full"]
    sep = "|" + "---|" * (head.count("|") - 1)
    return "\n".join([head, sep] + [row(e, lang, short) for e in items])


TABLES = yaml.safe_load((ROOT / "data/tables.yaml").read_text())
COLS = {
    "en": {"layer": ["Layer", "Principle", "Repos (⭐)", "How they differ", "Passes commercial detectors?"],
           "purpose": ["Purpose", "De-AI skills (⭐)", "Related writing suites (⭐)", "Choosing"]},
    "zh": {"layer": ["层次", "原理", "Repo（⭐）", "做法差异", "能否通过商业检测器"],
           "purpose": ["目的", "去 AI 味 Skill（⭐）", "相关写作套件（⭐）", "选用建议"]},
}
CJK_LANGS = {"zh-Hant", "ja", "ko"}


def repo_list(items):
    items = sorted(items, key=lambda e: -STARS.get(e["repo"], 0))
    out = []
    for e in items:
        name = e.get("name") or e["repo"].split("/")[1]
        out.append(f"[{name}](https://github.com/{e['repo']}) {fmt_stars(STARS.get(e['repo'], 0))}")
    return " · ".join(out) or "—"


def md_table(head, rows):
    lines = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    lines += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(lines)


def layer_table(lang):
    rows = []
    for L in TABLES["layers"]:
        t = L[lang]
        items = [e for e in entries if e["section"] in L["sections"]]
        repos = t.get("static") or repo_list(items)
        rows.append([f"**{t['layer']}**", t["principle"], repos, t["approach"], t["detectors"]])
    return md_table(COLS[lang]["layer"], rows)


def purpose_items(pid):
    skills = [e for e in entries if e["section"] in SKILL_SECTIONS]
    suites = [e for e in entries if e["section"] == "adjacent"]
    langs = lambda e: set(e.get("langs", []))
    pick = {
        "academic": lambda e: "academic" in e.get("use", []),
        "general-en": lambda e: "general" in e.get("use", []) and "en" in langs(e) and e["section"] != "upstream",
        "general-zh": lambda e: "general" in e.get("use", []) and "zh" in langs(e) and e["section"] != "upstream",
        "other-lang": lambda e: bool(langs(e) & CJK_LANGS),
        "fiction": lambda e: "fiction" in e.get("use", []),
        "social": lambda e: "social" in e.get("use", []),
        "tech-doc": lambda e: "tech-doc" in e.get("use", []),
    }
    if pid == "evasion":
        return [e for e in entries if e["section"] == "evasion"], []
    f = pick[pid]
    return [e for e in skills if f(e)], [e for e in suites if f(e)]


def purpose_table(lang):
    rows = []
    for P in TABLES["purposes"]:
        t = P[lang]
        sk, su = purpose_items(P["id"])
        rows.append([f"**{t['purpose']}**", repo_list(sk), repo_list(su), t["advice"]])
    return md_table(COLS[lang]["purpose"], rows)


def build(lang, out):
    text = (ROOT / f"templates/README.{lang}.md").read_text()
    text = text.replace("{{LAYER_TABLE}}", layer_table(lang)).replace("{{PURPOSE_TABLE}}", purpose_table(lang))
    text = re.sub(r"\{\{TABLE:(\w+)\}\}", lambda m: table(m.group(1), lang), text)
    text = text.replace("{{ASOF}}", AS_OF)
    n = len([e for e in entries if not e.get("research")])
    text = text.replace("{{COUNT}}", str(n))
    skills = [e for e in entries if e["section"] in SKILL_SECTIONS and STARS.get(e["repo"], 0) >= 1000]
    text = text.replace("{{SKILLS}}", str(len(skills)))
    header = "<!-- Generated by scripts/build_readme.py from data/ and templates/. Do not edit by hand. -->\n"
    (ROOT / out).write_text(header + text)


if __name__ == "__main__":
    figure.build_all(ROOT, entries, STARS, AS_OF)
    build("en", "README.md")
    build("zh", "README_zh.md")
    print("built README.md, README_zh.md, assets/fig1_en.svg, assets/fig1_zh.svg")

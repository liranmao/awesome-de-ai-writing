#!/usr/bin/env python3
"""Fig. 1 of the README: a journal-style schematic rendered as plain SVG.

Where de-AI interventions act and who examines each layer (curve width = number of listed tools).

Called by scripts/build_readme.py; writes assets/fig1_en.svg and assets/fig1_zh.svg.
Counts come from data/entries.yaml and data/stars.json.
"""
import json
from html import escape

FONT = "Helvetica Neue,Helvetica,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,sans-serif"
INK, GREY, LIGHT, RULE = "#1f1f1f", "#6b6b6b", "#a8a8a8", "#d9d9d9"
ACCENT = "#c0392b"  # mismatch annotation
LAYER_COL = {"L1": "#3b6ea8", "L2": "#d07a2d", "L3": "#4e9a6b", "L4": "#7a68a6"}
LAYER_FILL = {"L1": "#eaf1f8", "L2": "#fbf0e4", "L3": "#e8f3ec", "L4": "#efecf6"}
TIMING_COL = {"post-hoc": "#4d4d4d", "generation": "#9a9a9a", "model": "#cfcfcf", "none": "#ffffff"}

T = {
    "en": {
        "a": "Where interventions act, and who examines each layer",
        "col_left": "Intervention (timing)", "col_mid": "Layer of machine signature", "col_right": "Principal examiner",
        "timing": {"model": ["Modify model weights"], "generation": ["Constrain during", "generation"],
                   "post-hoc": ["Rewrite after", "drafting"]},
        "timing_eg": {"model": "e.g. heretic", "generation": "system prompts, material-first drafting",
                      "post-hoc": "rewriting skills, evasion tools"},
        "layers": {
            "L1": ("① Watermark", "Statistical bias introduced at sampling by the provider"),
            "L2": ("② Wording and syntax", "Stock vocabulary, em dashes, “not X but Y”, forced triads"),
            "L3": ("③ Structure and argument", "Templated paragraphs, formulaic order, claims without evidence"),
            "L4": ("④ Token distribution", "How predictable each token is under a language model"),
        },
        "exam": {
            "L1": ["Key-holding provider", "(SynthID)"],
            "L2": ["Human readers;", "rule-based linters"],
            "L3": ["Experienced readers; structure", "detectors (StoryScope, IdeaLens)"],
            "L4": ["Commercial detectors (GPTZero,", "Pangram, Turnitin, CNKI, Zhuque)"],
        },
        "mismatch": "Layer mismatch: most rewriting skills edit ②, whereas commercial detectors score ④",
        "arrow_note": "Arrow width ∝ number of listed tools",
        "b": "Listed tools per layer",
        "b_x": "Number of tools", "stars": "★", "stars_note": "★ = total GitHub stars",
        "timing_short": {"post-hoc": "After drafting", "generation": "During generation", "model": "Model weights", "none": "Toolkits (no timing)"},
        "c": "Benchmark: one abstract, six skills (Box 1)",
        "c_cols": ["Rule-based score", "GPTZero", "Facts"],
        "nt": "n.t.", "kept": "kept", "lost": "altered",
        "rows": {"orig_en": "Original (LLM)", "humanizer": "humanizer", "stopslop": "stop-slop",
                 "academic": "academic-humanizer", "antidefensive": "anti-defensive-writing", "human": "Human, 2020"},
        "c_note": "n.t., not tested (free quota exhausted). Single source text, one run per skill.",
        "title": "Fig. 1 | A layer-based view of de-AI writing tools",
    },
    "zh": {
        "a": "干预作用于哪一层，以及各层由谁识别",
        "col_left": "干预方式（时机）", "col_mid": "机器痕迹所在层次", "col_right": "主要识别者",
        "timing": {"model": ["修改模型权重"], "generation": ["生成过程中约束"], "post-hoc": ["成稿后改写"]},
        "timing_eg": {"model": "如 heretic", "generation": "系统提示词、先清点素材再写",
                      "post-hoc": "改写 Skill、绕检测工具"},
        "layers": {
            "L1": ("① 水印", "模型提供方在采样时引入的统计偏置"),
            "L2": ("② 用词与句式", "套话、破折号、“不是……而是……”、硬凑三段式"),
            "L3": ("③ 结构与论证", "模板化段落、程式化论证顺序、主张缺乏证据"),
            "L4": ("④ 词元概率分布", "每个词元在语言模型下的可预测程度"),
        },
        "exam": {
            "L1": ["持有密钥的提供方", "（SynthID）"],
            "L2": ["人类读者；", "规则检测器"],
            "L3": ["有经验的读者；结构级", "检测器（StoryScope、IdeaLens）"],
            "L4": ["商业检测器（GPTZero、Pangram、", "Turnitin、知网、朱雀）"],
        },
        "mismatch": "层次错位：多数改写 Skill 作用于第②层，而商业检测器测量的是第④层",
        "arrow_note": "箭头粗细 ∝ 收录工具数",
        "b": "各层收录工具数",
        "b_x": "工具数", "stars": "★", "stars_note": "★ = GitHub 星数之和",
        "timing_short": {"post-hoc": "成稿后", "generation": "生成中", "model": "改权重", "none": "工具包（无时机）"},
        "c": "实测：同一段摘要，六个 Skill（专栏 1）",
        "c_cols": ["规则检测分", "GPTZero", "事实"],
        "nt": "未测", "kept": "保留", "lost": "改动",
        "rows": {"orig_en": "原文（LLM）", "humanizer": "humanizer", "stopslop": "stop-slop",
                 "academic": "academic-humanizer", "antidefensive": "anti-defensive-writing", "human": "人类摘要，2020"},
        "c_note": "未测：免费额度用尽。单一源文本，每个 Skill 运行一次。",
        "title": "图 1｜从层次视角看去 AI 味工具",
    },
}



class Svg:
    def __init__(self, w, h):
        self.w, self.h, self.parts = w, h, []

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, size=12, fill=INK, weight="normal", anchor="start", style="normal"):
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" font-weight="{weight}" '
                 f'font-style="{style}" text-anchor="{anchor}">{escape(s)}</text>')

    def lines(self, x, y, rows, size=12, lh=None, **kw):
        lh = lh or size * 1.3
        for i, r in enumerate(rows):
            self.text(x, y + i * lh, r, size=size, **kw)

    def rect(self, x, y, w, h, fill="none", stroke="none", sw=1, rx=0, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def line(self, x1, y1, x2, y2, stroke=INK, sw=1, dash=None, marker=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        m = f' marker-end="url(#{marker})"' if marker else ""
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" '
                 f'stroke-width="{sw}"{d}{m}/>')

    def path(self, d, stroke=INK, sw=1, fill="none", marker=None, opacity=1):
        m = f' marker-end="url(#{marker})"' if marker else ""
        self.add(f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}" opacity="{opacity}"{m}/>')

    def render(self):
        defs = ['<defs>']
        for name, col in [("ah", GREY), ("ahk", INK), ("ahr", ACCENT)] + [(f"ah{k}", v) for k, v in LAYER_COL.items()]:
            defs.append(f'<marker id="{name}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
                        f'orient="auto-start-reverse" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker>')
        defs.append('</defs>')
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
                f'viewBox="0 0 {self.w} {self.h}" font-family="{FONT}">')
        return "\n".join([head, *defs, f'<rect width="{self.w}" height="{self.h}" fill="#ffffff"/>', *self.parts, "</svg>"])


def tool_layers(e):
    return [L for L in e["layer"].replace("L2-3", "L2,L3").split(",") if L]


def make(lang, entries, stars, scores, as_of):
    t = T[lang]
    tools = [e for e in entries if e["section"] not in ("adjacent", "detection")]
    W, H = 1200, 430
    s = Svg(W, H)

    # ---------------- panel a ----------------
    s.text(20, 34, t["a"], size=15, weight="bold")
    LX, LW = 30, 220          # intervention column
    MX, MW = 400, 400         # layer stack
    RX, RW = 900, 280         # examiner column
    top, rh, gap = 92, 62, 12
    for x, w, lab in [(LX, LW, t["col_left"]), (MX, MW, t["col_mid"]), (RX, RW, t["col_right"])]:
        s.text(x + w / 2, 68, lab, size=12, fill=GREY, anchor="middle", weight="bold")
        s.line(x, 76, x + w, 76, stroke=RULE)

    order = ["L1", "L2", "L3", "L4"]
    row_y = {L: top + i * (rh + gap) for i, L in enumerate(order)}
    for L in order:
        y = row_y[L]
        s.rect(MX, y, MW, rh, fill=LAYER_FILL[L], stroke=LAYER_COL[L], sw=1.2, rx=4)
        s.rect(MX, y, 6, rh, fill=LAYER_COL[L], rx=2)
        name, desc = t["layers"][L]
        s.text(MX + 18, y + 26, name, size=14, weight="bold", fill=LAYER_COL[L])
        s.text(MX + 18, y + 46, desc, size=11.5, fill=GREY)
        # examiner
        ex = t["exam"][L]
        s.lines(RX + 8, y + rh / 2 - (len(ex) - 1) * 8 + 4, ex, size=12, lh=16)
        s.line(MX + MW + 6, y + rh / 2, RX - 6, y + rh / 2, stroke=LAYER_COL[L], sw=1.4, marker=f"ah{L}")

    # intervention boxes, arrow width by number of tools that target each layer
    timings = ["model", "generation", "post-hoc"]
    box_y = {"model": top + 4, "generation": top + 112, "post-hoc": top + 214}
    bh = 70
    flows = {(tm, L): 0 for tm in timings for L in order}
    for e in tools:
        if e.get("timing"):
            for L in tool_layers(e):
                flows[(e["timing"], L)] += 1
    for tm in timings:
        y = box_y[tm]
        n = sum(1 for e in tools if e.get("timing") == tm)
        s.rect(LX, y, LW, bh, fill="#f6f6f6", stroke=LIGHT, rx=4)
        lab = t["timing"][tm]
        s.lines(LX + 12, y + 22, lab, size=13, weight="bold", lh=16)
        s.text(LX + 12, y + bh - 12, t["timing_eg"][tm], size=10.5, fill=GREY)
        s.text(LX + LW - 10, y + 20, f"n = {n}", size=11, fill=GREY, anchor="end")
        k = 0
        targets = [L for L in order if flows[(tm, L)]]
        for L in targets:
            c = flows[(tm, L)]
            x0, y0 = LX + LW, y + bh / 2 + (k - (len(targets) - 1) / 2) * 10
            x1, y1 = MX - 8, row_y[L] + rh / 2 + (timings.index(tm) - 1) * 17
            sw = 1 + 0.75 * c
            s.path(f"M{x0:.1f},{y0:.1f} C{x0 + 80:.1f},{y0:.1f} {x1 - 80:.1f},{y1:.1f} {x1:.1f},{y1:.1f}",
                   stroke=LAYER_COL[L], sw=sw, opacity=0.55)
            s.text(x1 - 4 if sw < 6 else x1 - 22, y1 + 3.5 if sw < 6 else y1 + sw / 2 + 12, str(c), size=10, fill=LAYER_COL[L], anchor="end", weight="bold")
            k += 1
    s.text(LX, top + 4 * (rh + gap) + 14, t["arrow_note"], size=10.5, fill=GREY, style="italic")

    # mismatch: red bracket linking ② and ④ on the examiner side, note beneath the stack
    bx = MX + MW + 22
    y2, y4 = row_y["L2"] + rh / 2, row_y["L4"] + rh / 2
    s.path(f"M{bx - 10},{y2} L{bx},{y2} L{bx},{y4} L{bx - 10},{y4}", stroke=ACCENT, sw=1.6)
    s.text(MX + MW / 2, top + 4 * (rh + gap) + 14, t["mismatch"], size=11.5, fill=ACCENT, weight="bold", anchor="middle")
    return s.render()


def build_all(root, entries, stars, as_of):
    scores = None
    (root / "assets").mkdir(exist_ok=True)
    for lang in ("en", "zh"):
        (root / f"assets/fig1_{lang}.svg").write_text(make(lang, entries, stars, scores, as_of))

# Awesome De-AI Writing

A survey-style collection of skills, tools, detectors and research on making AI-assisted writing read less like AI. Entries are organized by **mechanism** (which layer of "AI-ness" a tool acts on), and tagged by use case.

[中文版](README_zh.md) · {{COUNT}} entries · stars as of {{ASOF}}, refreshed weekly

![Where de-AI tools work](assets/layers.svg)

## Contents

- [Why organize by mechanism](#why-organize-by-mechanism)
- [A four-layer taxonomy](#a-four-layer-taxonomy)
- [Quick picks by use case](#quick-picks-by-use-case)
- [Catalog](#catalog)
- [Research](#research)
- [News and policy](#news-and-policy)
- [Responsible use](#responsible-use)
- [Contributing](#contributing)

## Why organize by mechanism

Most popular "humanizer" skills edit word choice and punctuation. Commercial detectors mostly score something else: how predictable each token is. That mismatch explains the most common surprise in this space: a rewrite that a reader finds clean can still score 100% AI. Sorting tools by the layer they act on tells you what a tool can and cannot do before you install it.

**Inclusion.** Tools need at least 1,000 GitHub stars. Watermarking and detection code tied to a peer-reviewed paper is included regardless of stars and marked 📄. Tools marketed for evading detectors are listed for completeness and marked ⚠️.

## A four-layer taxonomy

| Layer | What it is | Who checks it | Can a skill fix it? |
|---|---|---|---|
| ① Watermark | A statistical signal the provider embeds while generating | The provider holding the key (e.g. SynthID) | Heavy paraphrasing removes it, at a cost in quality |
| ② Wording & syntax | Stock words, dashes, "not X but Y", forced triads, filler | Readers; rule-based linters | Yes. Almost every popular skill works here |
| ③ Structure & argument | Paragraph templates, argument order, over-explained themes, claims without evidence | Experienced readers; structure-level detectors such as IdeaLens | Partly; a handful of skills try |
| ④ Token distribution | Whether each token is the predictable one | GPTZero, Pangram, Turnitin, CNKI, Zhuque | Barely, because the rewriter is still an LLM |

A second axis is **timing**: most tools rewrite after drafting; a few shape the text while it is written (system prompts, material-first writing); one changes the model weights.

## Quick picks by use case

- **English papers and grants:** [academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) keeps every number and citation and checks that verbs match the evidence. Avoid [stop-slop](https://github.com/hardikpandya/stop-slop) on scientific text: it bans passive voice, and its "two items instead of three" rule can drop list items.
- **General English prose:** [humanizer](https://github.com/blader/humanizer).
- **Chinese:** [Humanizer-zh](https://github.com/op7418/Humanizer-zh) for a full pass, [说人话](https://github.com/MrGeDiao/shuorenhua) for minimal edits, [lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone) for a metric-based report first.
- **Fiction and narrative:** [sepia](https://github.com/Nanako0129/sepia).
- **Prevent instead of fix:** [talk-normal](https://github.com/hexiecs/talk-normal), [human-writing](https://github.com/KKKKhazix/human-writing).

## Catalog

### Layer ② Wording and syntax: pattern editors

{{TABLE:wording}}

### Layer ②→③ Data-calibrated

{{TABLE:calibrated}}

### Layer ③ Structure and argument

{{TABLE:structure}}

### Upstream: prevent at generation or in the model

{{TABLE:upstream}}

### Layer ④ Detector-evasion tools ⚠️

Claims below are the authors' own and unverified. Pangram's DAMAGE study found that all 19 humanizers it audited degraded text quality. Submitting evasion-processed text as your own may breach academic-integrity rules.

{{TABLE:evasion}}

### Layer ① Watermarking

No text-watermark removal tool reaches 1,000 stars; paraphrasing already removes text watermarks.

{{TABLE:watermark}}

### Open-source detectors and benchmarks

{{TABLE:detection}}

### Adjacent: writing suites with a de-AI step

{{TABLE:adjacent}}

## Research

**How much AI is in scientific writing**
- Kobak et al., *Science Advances* 2025. [Delving into LLM-assisted writing in biomedical publications through excess vocabulary](https://arxiv.org/abs/2406.07016). At least 13.5% of 2024 PubMed abstracts were processed with LLMs; code: [berenslab/llm-excess-vocab](https://github.com/berenslab/llm-excess-vocab).
- Liang et al., *Nature Human Behaviour* 2025. [Quantifying large language model usage in scientific papers](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf). 22.5% of computer-science abstract sentences were LLM-modified by Sept 2024.

**Detection and its limits**
- Liang et al., *Patterns* 2023. [GPT detectors are biased against non-native English writers](https://www.eurekalert.org/news-releases/994660). Seven detectors labeled over half of TOEFL essays as AI.
- Masrour, Emi & Spero (Pangram Labs), 2025. [DAMAGE: Detecting Adversarially Modified AI Generated Text](https://arxiv.org/abs/2501.03437). All humanizers degraded quality; GPTZero's recall fell from 99.73% to 60.04% on humanized text; DIPPER paraphrasing cut SynthID detection from 87.6% to 5.4%.
- Russell et al., 2026. [StoryScope](https://arxiv.org/abs/2604.03136). Narrative-structure features alone detect AI fiction at 93.2% macro-F1, even after human editors rewrite the surface style.
- University of Maryland, 2026. [IdeaLens](https://arxiv.org/abs/2610.06778). Detection from concepts and argument structure rather than wording.
- Peer review: Pangram estimated about 21% of ICLR 2026 reviews were fully AI-generated, as reported by Nature news and cited in [arXiv 2602.00319](https://arxiv.org/abs/2602.00319).

**Watermarking**
- Dathathri et al., *Nature* 2024. [Scalable watermarking for identifying large language model outputs](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11499265/) (SynthID-Text).
- Kirchenbauer et al., ICML 2023. A Watermark for Large Language Models ([code](https://github.com/jwkirchenbauer/lm-watermarking)).

## News and policy

- Nature news, Jul 2026. ['Humanizer' tool can erase signs of AI-written text — alarming scientists](https://www.nature.com/articles/d41586-026-02105-3).
- The Register, 8 Jul 2026. [Tool promises to make lazy academics' AI-written papers sound more human](https://www.theregister.com/a/5268460).
- TechCrunch, 20 Nov 2025. [The best guide to spotting AI writing comes from Wikipedia](https://techcrunch.com/2025/11/20/the-best-guide-to-spotting-ai-writing-comes-from-wikipedia/). Source guide: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- 36Kr, May 2026. [论文 AI 检测，正在逼疯这届大学生](https://www.36kr.com/p/3823851041476992). A classic Chinese essay scored 62.88% AI.
- CCTV via Guangming, 22 May 2026. [毕业论文将检测AIGC率，检测标准科学吗？](https://m.gmw.cn/2026-05/22/content_1304466247.htm) Thresholds of 15–40% at Chinese universities.
- Policies: [Nature Portfolio AI policy](https://www.nature.com/nature-portfolio/editorial-policies/ai) (language polishing permitted; extensive writing support needs disclosure) · [Science journals](https://www.timeshighereducation.com/node/729880) (disclose the tool, version and full prompt).

## Responsible use

Use these tools to make your own writing clearer, not to hide that AI was involved. Check every number and claim after a rewrite; some skills drop facts or strengthen claims. Follow your venue's disclosure rules regardless of what a detector says.

## Contributing

Add or fix an entry in [data/entries.yaml](data/entries.yaml), run `python scripts/build_readme.py`, and open a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion criteria and how to classify a tool's layer.

## License

[CC0 1.0](LICENSE). Linked projects keep their own licenses.

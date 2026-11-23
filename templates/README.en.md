# Awesome De-AI Writing

## Practical guide

| What you are writing | Use | Avoid |
|---|---|---|
| English papers and grants | [academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) (keeps numbers and citations, checks that verbs match the evidence); [humanizer](https://github.com/blader/humanizer) for general polishing | [stop-slop](https://github.com/hardikpandya/stop-slop) (bans passive voice), [anti-defensive-writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) (drops unfavorable results) |
| Chinese STEM papers | [Humanizer-zh](https://github.com/op7418/Humanizer-zh) (keeps academic register, passive voice and terminology) | detector-evasion tools |
| Chinese humanities papers | [说人话](https://github.com/MrGeDiao/shuorenhua) if you quote heavily (leaves quotations and references untouched), or [Humanizer-zh](https://github.com/op7418/Humanizer-zh) for a fuller pass; then [writing-dna-skill](https://github.com/larashero3-dotcom/writing-dna-skill) trained on your own earlier writing to keep your voice; add [Awesome-Journal-Skills](https://github.com/brycewang-stanford/Awesome-Journal-Skills) when targeting a specific social-science journal | [human-writing](https://github.com/KKKKhazix/human-writing) (pushes toward conversational tone), [anti-defensive-writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) (built around experiments and metrics) |
| Blogs, newsletters, social posts | [human-writing](https://github.com/KKKKhazix/human-writing) (Chinese), [humanizer](https://github.com/blader/humanizer) (English) | — |
| Fiction and narrative | [sepia](https://github.com/Nanako0129/sepia) | — |
| Prevent rather than fix | [talk-normal](https://github.com/hexiecs/talk-normal) (a system prompt) | — |

Four rules before you start:

1. **Know what you want.** These tools make text easier to read; they rarely change what GPTZero, Turnitin or CNKI report (see Fig. 1).
2. **Give a writing sample if you have one.** humanizer, academic-humanizer and writing-dna-skill can match your own prior writing.
3. **Check everything afterwards:** numbers, quotations, hedges ("may", "suggest"), and whether unfavorable results survived.
4. **Disclose AI use as your venue requires**, regardless of any detector score.

***This repository collects {{SKILLS}} de-AI writing skills with more than 1,000 GitHub stars.***

[中文版](README_zh.md) · star counts as of {{ASOF}}, refreshed weekly

<p align="center"><img src="assets/fig1_en.svg" alt="Fig. 1: where de-AI tools act and who examines each layer" width="100%"></p>

**Fig. 1 | Where de-AI tools act and who examines each layer.** Centre, the four layers at which text can carry a machine signature. Left, interventions grouped by timing; curve width is proportional to the number of listed tools acting on each layer. Right, the principal examiner of each layer. The red annotation marks the mismatch between where most rewriting skills operate (②) and what commercial detectors measure (④).

## Table 1 | By mechanism

{{LAYER_TABLE}}

## Table 2 | By purpose

{{PURPOSE_TABLE}}

⚠️ Tools marketed for evading detectors are listed for completeness and not recommended; their claims are the authors' own and unverified. Whatever tool is used, check every number and claim after rewriting, and disclose AI use as your venue requires.

## Contributing

To add or correct an entry, edit [data/entries.yaml](data/entries.yaml) (row prose for the tables is in [data/tables.yaml](data/tables.yaml)), run `python scripts/build_readme.py` and open a pull request. Inclusion criteria and guidance on assigning a layer are in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[CC0 1.0](LICENSE). Linked projects retain their own licences.

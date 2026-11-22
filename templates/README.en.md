# Awesome De-AI Writing

***This repository collects {{SKILLS}} de-AI writing skills with more than 1,000 GitHub stars.***

[中文版](README_zh.md) · {{COUNT}} entries · star counts as of {{ASOF}}, refreshed weekly

> Large language models (LLMs) now contribute to a substantial fraction of the scientific literature<sup>[1](#ref-1),[2](#ref-2)</sup>, and an ecosystem of "humanizer" skills has emerged to make such text read as if written by a person. These tools are usually compared by popularity or by anecdote. Here we classify them instead by the layer of the text they modify — the generation-time watermark, surface wording, discourse structure or the token-probability distribution — and argue that this distinction largely accounts for their observed behaviour. Most widely adopted skills act on wording, whereas commercial detectors respond chiefly to token-level predictability; accordingly, a rewrite that reads as natural to a human may still be scored as fully machine-generated. We catalogue {{COUNT}} tools and resources against this taxonomy, summarize the evidence on detection and its limits, and outline principles for responsible use.

<p align="center"><img src="assets/fig1_en.svg" alt="Fig. 1: layer-based view of de-AI writing tools" width="100%"></p>

**Fig. 1 | A layer-based view of de-AI writing tools.** **a**, Four layers at which text can carry a machine signature (centre), the interventions that act on them, grouped by timing (left), and the principal examiner of each layer (right). Curve width is proportional to the number of listed tools acting on a given layer; tools that act on two layers contribute to both. The red bracket marks the mismatch between where most rewriting skills operate (②) and what commercial detectors measure (④). **b**, Number of listed tools per layer, stacked by timing, with the summed GitHub stars of those tools. Watermarking toolkits carry no timing. Detectors, benchmarks and adjacent writing suites are excluded. Panels **a** and **b** are regenerated from `data/entries.yaml` and `data/stars.json` at each build.

## Key points

- "AI-ness" in text is not a single property. It arises at four separable layers, each examined by different readers or detectors.
- The majority of popular de-AI skills operate on wording and syntax (layer ②), the layer most visible to human readers but least relevant to probability-based detectors (layer ④).
- Detection itself is unreliable at the margins: detectors misclassify non-native English writing<sup>[3](#ref-3)</sup>, and adversarial paraphrasing degrades both detector recall and watermark detection<sup>[4](#ref-4)</sup>.
- Emerging detectors that read narrative and argument structure<sup>[5](#ref-5),[6](#ref-6)</sup> suggest that surface-level rewriting will become less effective over time.
- These tools are appropriate for improving clarity, not for concealing AI involvement; disclosure obligations apply irrespective of any detector score<sup>[10](#ref-10),[11](#ref-11)</sup>.

## Contents

- [Introduction](#introduction)
- [A four-layer taxonomy](#a-four-layer-taxonomy)
- [Selecting a tool by use case](#selecting-a-tool-by-use-case)
- [Catalogue](#catalogue)
- [Evidence on prevalence, detection and watermarking](#evidence-on-prevalence-detection-and-watermarking)
- [News and editorial policy](#news-and-editorial-policy)
- [Outlook and open questions](#outlook-and-open-questions)
- [Responsible use](#responsible-use)
- [References](#references)
- [Contributing](#contributing)

## Introduction

Analyses of excess vocabulary estimate that at least 13.5% of PubMed abstracts published in 2024 were processed with an LLM<sup>[1](#ref-1)</sup>, and that up to 22.5% of sentences in computer-science abstracts had been LLM-modified by September 2024<sup>[2](#ref-2)</sup>. In parallel, open-source "humanizer" skills for coding agents have accumulated tens of thousands of GitHub stars, and their use in academic writing has attracted coverage in *Nature*<sup>[12](#ref-12)</sup>.

A recurring observation among users is that a rewrite judged clean by a human reader may still be scored as 100% AI-generated. We argue that this apparent paradox reflects a mismatch of layers: most skills edit word choice and punctuation, whereas commercial detectors primarily estimate how predictable each token is under a language model. Classifying tools by the layer on which they act therefore indicates, before installation, what a given tool can and cannot be expected to change.

**Inclusion criteria.** Tools are included if they have at least 1,000 GitHub stars. Watermarking and detection code accompanying a peer-reviewed publication is included regardless of star count and marked 📄. Tools marketed primarily for evading detectors are listed for completeness, marked ⚠️, and not endorsed.

## A four-layer taxonomy

**Table 1 | Layers at which text can carry a machine signature.**

| Layer | Definition | Principal examiner | Amenable to a rewriting skill? |
|---|---|---|---|
| ① Watermark | A statistical signal embedded by the provider during generation | The key-holding provider (for example, SynthID<sup>[8](#ref-8)</sup>) | Removable by extensive paraphrasing, at a measurable cost to quality<sup>[4](#ref-4)</sup> |
| ② Wording and syntax | Stock vocabulary, em dashes, "not X but Y" constructions, forced triads, filler | Human readers; rule-based linters | Yes; almost all widely used skills act here |
| ③ Structure and argument | Templated paragraphs, formulaic argument order, over-explained themes, claims unsupported by evidence | Experienced readers; structure-level detectors<sup>[5](#ref-5),[6](#ref-6)</sup> | Partially; a minority of skills attempt it |
| ④ Token distribution | The extent to which each token is the most probable continuation | GPTZero, Pangram, Turnitin, CNKI, Tencent Zhuque | Rarely, because the rewriter is itself an LLM |

A second, orthogonal axis is **timing**. Most tools rewrite text after it has been drafted (post hoc); a few constrain the text during generation, through system prompts or material-first drafting; and one modifies the model weights directly.

## Selecting a tool by use case

- **English manuscripts and grant proposals.** [academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) preserves every number and citation and checks that verbs do not overstate the evidence. [stop-slop](https://github.com/hardikpandya/stop-slop) is not recommended for scientific text, because it prohibits the passive voice.
- **General English prose.** [humanizer](https://github.com/blader/humanizer).
- **Chinese.** [Humanizer-zh](https://github.com/op7418/Humanizer-zh) for a comprehensive pass; [说人话](https://github.com/MrGeDiao/shuorenhua) for minimal intervention; [lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone) when a metric-based diagnostic report is wanted before rewriting.
- **Fiction and narrative.** [sepia](https://github.com/Nanako0129/sepia).
- **Prevention rather than correction.** [talk-normal](https://github.com/hexiecs/talk-normal) and [human-writing](https://github.com/KKKKhazix/human-writing).

## Catalogue

Within each table, entries are ordered by GitHub stars.

### Layer ② Wording and syntax: pattern-based editors

{{TABLE:wording}}

### Layers ②–③ Corpus-calibrated editors

{{TABLE:calibrated}}

### Layer ③ Structure and argument

{{TABLE:structure}}

### Upstream approaches: prevention during generation or in the model

{{TABLE:upstream}}

### Layer ④ Detector-evasion tools ⚠️

The efficacy claims below are made by the authors and have not been independently verified. The DAMAGE study found that all 19 humanizers it audited degraded text quality<sup>[4](#ref-4)</sup>. Submitting evasion-processed text as one's own work may contravene academic-integrity policies.

{{TABLE:evasion}}

### Layer ① Watermarking

No text-watermark removal tool currently exceeds 1,000 stars, in part because paraphrasing alone suffices to remove text watermarks<sup>[4](#ref-4)</sup>.

{{TABLE:watermark}}

### Open-source detectors and benchmarks

{{TABLE:detection}}

### Related writing suites with a de-AI step

{{TABLE:adjacent}}

## Evidence on prevalence, detection and watermarking

**Prevalence in the scientific literature.** Excess-vocabulary analysis indicates that at least 13.5% of 2024 PubMed abstracts were processed with an LLM<sup>[1](#ref-1)</sup> (code: [berenslab/llm-excess-vocab](https://github.com/berenslab/llm-excess-vocab)). A distributional estimate found that 22.5% of sentences in computer-science abstracts had been LLM-modified by September 2024<sup>[2](#ref-2)</sup>.

**Detection and its limitations.** Seven widely used detectors classified more than half of a set of TOEFL essays written by non-native English speakers as AI-generated<sup>[3](#ref-3)</sup>. In the DAMAGE audit, humanizer rewriting reduced GPTZero recall from 99.73% to 60.04%, and DIPPER paraphrasing reduced SynthID detection from 87.6% to 5.4%<sup>[4](#ref-4)</sup>. Conversely, structure-level methods appear more robust to surface editing: narrative-structure features alone identified AI-generated fiction with a macro-F1 of 93.2%, even after human editors had rewritten the prose style<sup>[5](#ref-5)</sup>, and IdeaLens detects AI text from concepts and argument structure rather than wording<sup>[6](#ref-6)</sup>. In peer review, Pangram estimated that approximately 21% of ICLR 2026 reviews were fully AI-generated<sup>[7](#ref-7)</sup>.

**Watermarking.** SynthID-Text embeds a tournament-sampling watermark at generation time and has been deployed at production scale<sup>[8](#ref-8)</sup>; the earlier green-list scheme of Kirchenbauer et al. partitions the vocabulary at each step and biases sampling towards a pseudorandom subset<sup>[9](#ref-9)</sup>.

## News and editorial policy

- *Nature* news, July 2026. ['Humanizer' tool can erase signs of AI-written text — alarming scientists](https://www.nature.com/articles/d41586-026-02105-3)<sup>[12](#ref-12)</sup>.
- *The Register*, 8 July 2026. [Tool promises to make lazy academics' AI-written papers sound more human](https://www.theregister.com/a/5268460).
- *TechCrunch*, 20 November 2025. [The best guide to spotting AI writing comes from Wikipedia](https://techcrunch.com/2025/11/20/the-best-guide-to-spotting-ai-writing-comes-from-wikipedia/); source guide: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- *36Kr*, May 2026. [论文 AI 检测，正在逼疯这届大学生](https://www.36kr.com/p/3823851041476992). A canonical modern Chinese essay was scored as 62.88% AI-generated.
- CCTV, via Guangming Online, 22 May 2026. [毕业论文将检测AIGC率，检测标准科学吗？](https://m.gmw.cn/2026-05/22/content_1304466247.htm) Chinese universities apply AIGC thresholds of 15–40%.
- **Editorial policies.** Nature Portfolio permits AI-assisted language editing but requires disclosure of more extensive writing support<sup>[10](#ref-10)</sup>; the *Science* journals require disclosure of the tool, its version and the full prompt<sup>[11](#ref-11)</sup>.

## Outlook and open questions

Three questions remain open. First, no tool in this catalogue has been shown to change layer-④ scores while preserving content; whether any LLM-based rewriter can do so is unresolved, given that the rewriter's own output distribution is what detectors measure. Second, as structure-level detectors mature<sup>[5](#ref-5),[6](#ref-6)</sup>, the advantage conferred by layer-② editing is likely to diminish, shifting attention to argument and evidence. Third, the false-positive rates documented for non-native writers<sup>[3](#ref-3)</sup> and for canonical human texts call into question the use of fixed detector thresholds in assessment. Systematic benchmarks spanning multiple texts, languages and detectors would help to address all three questions.

## Responsible use

These tools should be used to make one's own writing clearer, not to conceal the involvement of AI. Every number and claim should be verified after rewriting, because some skills omit facts or strengthen claims beyond the evidence. Authors should follow the disclosure requirements of the relevant journal, funder or institution irrespective of any detector result.

## References

1. <a name="ref-1"></a>Kobak, D., González-Márquez, R., Horvát, E.-Á. & Lause, J. Delving into LLM-assisted writing in biomedical publications through excess vocabulary. *Sci. Adv.* **11**, eadt3813 (2025). [doi:10.1126/sciadv.adt3813](https://doi.org/10.1126/sciadv.adt3813) · [arXiv](https://arxiv.org/abs/2406.07016)
   - *Estimates a lower bound on LLM processing across PubMed from shifts in word frequency.*
2. <a name="ref-2"></a>Liang, W. et al. Quantifying large language model usage in scientific papers. *Nat. Hum. Behav.* (2025). [doi:10.1038/s41562-025-02273-8](https://doi.org/10.1038/s41562-025-02273-8) · [PDF](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf)
3. <a name="ref-3"></a>Liang, W., Yuksekgonul, M., Mao, Y., Wu, E. & Zou, J. GPT detectors are biased against non-native English writers. *Patterns* **4**, 100779 (2023). [doi:10.1016/j.patter.2023.100779](https://doi.org/10.1016/j.patter.2023.100779)
   - *Documents systematic false positives against non-native writers.*
4. <a name="ref-4"></a>Masrour, E., Emi, B. & Spero, M. DAMAGE: detecting adversarially modified AI generated text. Preprint at [arXiv:2501.03437](https://arxiv.org/abs/2501.03437) (2025).
   - *The most direct audit of humanizers to date: quality degradation, detector recall and watermark removal.*
5. <a name="ref-5"></a>Russell et al. StoryScope. Preprint at [arXiv:2604.03136](https://arxiv.org/abs/2604.03136) (2026).
6. <a name="ref-6"></a>IdeaLens (University of Maryland). Preprint at [arXiv:2610.06778](https://arxiv.org/abs/2610.06778) (2026).
7. <a name="ref-7"></a>Estimate of AI-generated ICLR 2026 reviews by Pangram, as reported by *Nature* news and cited in [arXiv:2602.00319](https://arxiv.org/abs/2602.00319) (2026).
8. <a name="ref-8"></a>Dathathri, S. et al. Scalable watermarking for identifying large language model outputs. *Nature* **634**, 818–823 (2024). [doi:10.1038/s41586-024-08025-4](https://doi.org/10.1038/s41586-024-08025-4) · [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11499265/)
9. <a name="ref-9"></a>Kirchenbauer, J. et al. A watermark for large language models. In *Proc. 40th International Conference on Machine Learning* (ICML, 2023). [Code](https://github.com/jwkirchenbauer/lm-watermarking)
10. <a name="ref-10"></a>Nature Portfolio. Artificial intelligence (AI). Editorial policies. <https://www.nature.com/nature-portfolio/editorial-policies/ai>
11. <a name="ref-11"></a>*Science* journals' policy on AI disclosure, as reported by *Times Higher Education*. <https://www.timeshighereducation.com/node/729880>
12. <a name="ref-12"></a>'Humanizer' tool can erase signs of AI-written text — alarming scientists. *Nature* (news, July 2026). <https://www.nature.com/articles/d41586-026-02105-3>

## Contributing

To add or correct an entry, edit [data/entries.yaml](data/entries.yaml), run `python scripts/build_readme.py` and open a pull request. Inclusion criteria and guidance on assigning a layer are given in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[CC0 1.0](LICENSE). Linked projects retain their own licences.

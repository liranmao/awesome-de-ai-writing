# Awesome De-AI Writing｜去AI味工具综述

一份综述式合集：收录让 AI 辅助写作读起来不那么像 AI 的 Skill、工具、检测器和研究。按**原理**分类（工具作用在「AI 味」的哪一层），用途做标签。

[English](README.md) · 共 {{COUNT}} 项 · 星数截至 {{ASOF}}，每周自动更新

![去AI味工具作用在哪一层](assets/layers.svg)

## 目录

- [为什么按原理分类](#为什么按原理分类)
- [四层分类法](#四层分类法)
- [按场景速查](#按场景速查)
- [合集](#合集)
- [研究文献](#研究文献)
- [新闻与政策](#新闻与政策)
- [使用原则](#使用原则)
- [参与贡献](#参与贡献)

## 为什么按原理分类

高赞的 humanizer 类 Skill 大多在改用词和标点，而商业检测器主要测的是另一件事：每个词是不是「最好猜」的那个。两者错位，所以常见这种情况：读者觉得改得很干净，检测器照样判 100% AI。按作用层分类，装之前就能知道一个工具能做什么、做不到什么。

**收录标准**：工具需 GitHub 1,000 星以上；有同行评审论文的水印和检测代码不限星数，标 📄；以绕过检测为卖点的工具为完整起见列出，标 ⚠️。

## 四层分类法

| 层 | 是什么 | 谁在查 | Skill 能不能改 |
|---|---|---|---|
| ① 水印 | 模型生成时埋进去的统计信号 | 持有密钥的厂商（如 SynthID） | 大幅改写能洗掉，但会牺牲文字质量 |
| ② 用词和句式 | 套话、破折号、「不是…而是…」、硬凑三段式 | 读者、规则检测器 | 能，几乎所有高赞 Skill 都在这一层 |
| ③ 结构和论证 | 段落套路、论证顺序、把主题讲透替读者总结、主张没有证据 | 有经验的读者、IdeaLens 等结构级检测器 | 部分能，少数 Skill 在尝试 |
| ④ 词的概率分布 | 每个词是不是最可预测的那个 | GPTZero、Pangram、Turnitin、知网、朱雀 | 基本不能，因为改写的还是 AI |

第二条轴是**时机**：大多数工具写完再改；少数在写的时候就规避（系统提示词、先清点材料再写）；还有一个直接改模型权重。

## 按场景速查

- **英文论文和基金**：[academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer)，数字和引用一个不改，还检查动词是否强于证据。科研文本别用 [stop-slop](https://github.com/hardikpandya/stop-slop)：它禁被动语态，「三项改两项」的规则还可能删掉列举项。
- **通用英文**：[humanizer](https://github.com/blader/humanizer)。
- **中文**：全面改用 [Humanizer-zh](https://github.com/op7418/Humanizer-zh)；只想轻改用 [说人话](https://github.com/MrGeDiao/shuorenhua)；想先看量化报告用 [lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone)。
- **小说和叙事**：[sepia](https://github.com/Nanako0129/sepia)。
- **从源头避免**：[talk-normal](https://github.com/hexiecs/talk-normal)、[human-writing](https://github.com/KKKKhazix/human-writing)。

## 合集

### 第②层 用词和句式：规则清单派

{{TABLE:wording}}

### 第②→③层 数据校准派

{{TABLE:calibrated}}

### 第③层 结构和论证

{{TABLE:structure}}

### 源头派：写时规避或改模型

{{TABLE:upstream}}

### 第④层 降 AIGC / 绕检测工具 ⚠️

以下效果均为作者自述、未经验证。Pangram 的 DAMAGE 研究审查了 19 个 humanizer，全部会降低文字质量。把这类工具处理过的文本当作自己的成果提交，可能违反学术诚信规定。

{{TABLE:evasion}}

### 第①层 水印

没有过 1,000 星的文本去水印工具；大幅改写本身就能洗掉文本水印。

{{TABLE:watermark}}

### 开源检测器与基准

{{TABLE:detection}}

### 相关：带去AI味步骤的写作套件

{{TABLE:adjacent}}

## 研究文献

**科研写作里有多少 AI**
- Kobak 等，*Science Advances* 2025。[Delving into LLM-assisted writing in biomedical publications through excess vocabulary](https://arxiv.org/abs/2406.07016)。2024 年至少 13.5% 的 PubMed 摘要经过 LLM 处理；代码 [berenslab/llm-excess-vocab](https://github.com/berenslab/llm-excess-vocab)。
- Liang 等，*Nature Human Behaviour* 2025。[Quantifying large language model usage in scientific papers](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf)。截至 2024 年 9 月，计算机科学摘要中 22.5% 的句子经 LLM 修改。

**检测及其局限**
- Liang 等，*Patterns* 2023。[GPT detectors are biased against non-native English writers](https://www.eurekalert.org/news-releases/994660)。7 个检测器把超过一半的托福作文判为 AI。
- Masrour、Emi、Spero（Pangram Labs），2025。[DAMAGE](https://arxiv.org/abs/2501.03437)。所有 humanizer 都降低文字质量；GPTZero 对 humanizer 改写文本的检出率从 99.73% 降到 60.04%；DIPPER 改写让 SynthID 检出率从 87.6% 降到 5.4%。
- Russell 等，2026。[StoryScope](https://arxiv.org/abs/2604.03136)。只用叙事结构特征检测 AI 小说，macro-F1 达 93.2%，人工改写表层文风后依然有效。
- 马里兰大学，2026。[IdeaLens](https://arxiv.org/abs/2610.06778)。从观点和论证结构而非用词来检测。
- 审稿：Pangram 估计 ICLR 2026 约 21% 的审稿意见完全由 AI 生成（Nature 新闻报道，[arXiv 2602.00319](https://arxiv.org/abs/2602.00319) 引用）。

**水印**
- Dathathri 等，*Nature* 2024。[Scalable watermarking for identifying large language model outputs](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11499265/)（SynthID-Text）。
- Kirchenbauer 等，ICML 2023。A Watermark for Large Language Models（[代码](https://github.com/jwkirchenbauer/lm-watermarking)）。

## 新闻与政策

- Nature 新闻，2026-07。['Humanizer' tool can erase signs of AI-written text — alarming scientists](https://www.nature.com/articles/d41586-026-02105-3)。
- The Register，2026-07-08。[Tool promises to make lazy academics' AI-written papers sound more human](https://www.theregister.com/a/5268460)。
- TechCrunch，2025-11-20。[The best guide to spotting AI writing comes from Wikipedia](https://techcrunch.com/2025/11/20/the-best-guide-to-spotting-ai-writing-comes-from-wikipedia/)。原始指南：[Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)。
- 36氪，2026-05。[论文 AI 检测，正在逼疯这届大学生](https://www.36kr.com/p/3823851041476992)。《荷塘月色》被测出 62.88% AI 率。
- 央视新闻（光明网转载），2026-05-22。[毕业论文将检测AIGC率，检测标准科学吗？](https://m.gmw.cn/2026-05/22/content_1304466247.htm) 各校门槛 15%–40%。
- 期刊政策：[Nature Portfolio](https://www.nature.com/nature-portfolio/editorial-policies/ai)（允许语言润色，大量写作支持需披露）· [Science 系列](https://www.timeshighereducation.com/node/729880)（写明工具、版本和完整 prompt）。

## 使用原则

用这些工具让你自己的文字更清楚，而不是掩盖用过 AI。改写后逐一核对数字和结论，有些 Skill 会删事实或加强主张。无论检测器怎么判，都按投稿方的要求披露 AI 使用。

## 参与贡献

在 [data/entries.yaml](data/entries.yaml) 里新增或修改条目，运行 `python scripts/build_readme.py`，然后提交 PR。收录标准和分层方法见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

[CC0 1.0](LICENSE)。所链接项目沿用各自的许可。

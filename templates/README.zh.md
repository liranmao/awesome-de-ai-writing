# Awesome De-AI Writing｜去 AI 味工具综述

***本 GitHub repo 包含了 {{SKILLS}} 个 >1000 star 的去 AI 味 Skill。***

[English](README.md) · 共收录 {{COUNT}} 项 · 星数截至 {{ASOF}}，每周自动更新

> 大语言模型（LLM）已参与相当比例的科研文献写作<sup>[1](#ref-1),[2](#ref-2)</sup>，随之出现了一批旨在让此类文本"读起来像人写的"humanizer 类 Skill。现有比较多依据热度或个人体验。本文改以工具所作用的文本层次为分类依据——生成时水印、表层用词、篇章结构与词元概率分布——并认为这一区分在很大程度上可以解释工具的实际表现：主流 Skill 大多作用于用词层，而商业检测器主要响应词元层面的可预测性。因此，人类读来自然的改写文本，仍可能被判定为完全由机器生成。本文据此分类法整理了 {{COUNT}} 项工具与资源，归纳关于检测及其局限的现有证据，并提出负责任使用的原则。

<p align="center"><img src="assets/fig1_zh.svg" alt="图 1：从层次视角看去 AI 味工具" width="100%"></p>

**图 1｜从层次视角看去 AI 味工具。** **a**，文本可能携带机器痕迹的四个层次（中）、按时机分组的作用于各层的干预方式（左），以及各层的主要识别者（右）。曲线粗细与作用于该层的收录工具数成正比；同时作用于两层的工具在两层均计入。红色括线标示层次错位：多数改写 Skill 作用于第②层，而商业检测器测量的是第④层。**b**，各层收录工具数，按时机堆叠，并标注这些工具的 GitHub 星数之和。水印工具包无时机属性。检测器、基准与相关写作套件不计入。**a**、**b** 两图在每次构建时依据 `data/entries.yaml` 与 `data/stars.json` 自动重绘。

## 要点

- 文本的"AI 味"并非单一属性，而是产生于四个可分离的层次，分别由不同的读者或检测器识别。
- 多数高星 Skill 作用于用词与句式（第②层）：这一层对人类读者最为显眼，对基于概率的检测器（第④层）却影响最小。
- 检测本身在边界情形下并不可靠：检测器会误判非英语母语者的写作<sup>[3](#ref-3)</sup>，对抗性改写会同时降低检测器召回率与水印检出率<sup>[4](#ref-4)</sup>。
- 基于叙事与论证结构的新型检测器<sup>[5](#ref-5),[6](#ref-6)</sup>提示，仅改写表层的做法其效果可能逐渐减弱。
- 这些工具适用于提升表达清晰度，而非掩盖 AI 参与；无论检测结果如何，均应履行披露义务<sup>[10](#ref-10),[11](#ref-11)</sup>。

## 目录

- [引言](#引言)
- [四层分类法](#四层分类法)
- [按使用场景选择工具](#按使用场景选择工具)
- [工具合集](#工具合集)
- [关于普及程度、检测与水印的证据](#关于普及程度检测与水印的证据)
- [新闻与期刊政策](#新闻与期刊政策)
- [展望与待解问题](#展望与待解问题)
- [使用原则](#使用原则)
- [参考文献](#参考文献)
- [参与贡献](#参与贡献)

## 引言

基于超额词汇的分析估计，2024 年发表的 PubMed 摘要中至少 13.5% 经过 LLM 处理<sup>[1](#ref-1)</sup>；截至 2024 年 9 月，计算机科学摘要中高达 22.5% 的句子经过 LLM 修改<sup>[2](#ref-2)</sup>。与此同时，面向编程智能体的开源 humanizer 类 Skill 已累计数万 GitHub 星标，其在学术写作中的使用也引起了 *Nature* 新闻的关注<sup>[12](#ref-12)</sup>。

用户中反复出现的一种现象是：人类读者认为已改得很自然的文本，检测器仍判定为 100% AI 生成。本文认为，这一看似矛盾的现象源于层次错位：多数 Skill 修改的是用词和标点，而商业检测器主要估计的是每个词元在语言模型下的可预测程度。因此，按作用层次对工具进行分类，可在安装之前判断某一工具能够改变什么、不能改变什么。

**收录标准。** 工具须获得至少 1,000 个 GitHub 星标。随同行评审论文发布的水印与检测代码不受星数限制，以 📄 标注。以绕过检测为主要卖点的工具出于完整性列出，以 ⚠️ 标注，本文不予推荐。

## 四层分类法

**表 1｜文本可能携带机器痕迹的层次**

| 层次 | 定义 | 主要识别者 | 可否通过改写 Skill 消除 |
|---|---|---|---|
| ① 水印 | 模型提供方在生成过程中嵌入的统计信号 | 持有密钥的提供方（如 SynthID<sup>[8](#ref-8)</sup>） | 大幅改写可消除，但会造成可测量的质量损失<sup>[4](#ref-4)</sup> |
| ② 用词与句式 | 套话、破折号、"不是……而是……"句式、硬凑三段式、冗余表达 | 人类读者；规则检测器 | 可以；几乎所有主流 Skill 均作用于此层 |
| ③ 结构与论证 | 模板化段落、程式化论证顺序、替读者过度总结、主张缺乏证据支撑 | 经验丰富的读者；结构级检测器<sup>[5](#ref-5),[6](#ref-6)</sup> | 部分可以；少数 Skill 有所尝试 |
| ④ 词元概率分布 | 每个词元是否为最可能的续写 | GPTZero、Pangram、Turnitin、知网、腾讯朱雀 | 基本不能，因为改写者本身仍是 LLM |

另一条正交的分类轴是**时机**：多数工具在成稿后改写（事后改写）；少数在生成过程中加以约束（系统提示词，或先清点素材再动笔）；另有一项工具直接修改模型权重。

## 按使用场景选择工具

- **英文论文与基金申请书。** [academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) 保留全部数字与引用，并检查动词强度是否超出证据支持。不建议将 [stop-slop](https://github.com/hardikpandya/stop-slop) 用于科研文本，因为该工具禁用被动语态。
- **通用英文写作。** [humanizer](https://github.com/blader/humanizer)。
- **中文写作。** 全面修改可选 [Humanizer-zh](https://github.com/op7418/Humanizer-zh)；最小幅度修改可选 [说人话](https://github.com/MrGeDiao/shuorenhua)；如需在改写前获得量化诊断报告，可选 [lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone)。
- **小说与叙事文本。** [sepia](https://github.com/Nanako0129/sepia)。
- **源头预防而非事后修正。** [talk-normal](https://github.com/hexiecs/talk-normal) 与 [human-writing](https://github.com/KKKKhazix/human-writing)。

## 工具合集

各表内条目按 GitHub 星数降序排列。

### 第②层 用词与句式：基于规则清单的编辑工具

{{TABLE:wording}}

### 第②–③层 基于语料校准的编辑工具

{{TABLE:calibrated}}

### 第③层 结构与论证

{{TABLE:structure}}

### 源头方法：在生成阶段或模型层面预防

{{TABLE:upstream}}

### 第④层 降 AIGC 率／绕过检测工具 ⚠️

以下效果均为作者自述，未经独立验证。DAMAGE 研究审查的 19 个 humanizer 均降低了文本质量<sup>[4](#ref-4)</sup>。将此类工具处理过的文本作为本人成果提交，可能违反学术诚信规定。

{{TABLE:evasion}}

### 第①层 水印

目前尚无文本去水印工具超过 1,000 星，部分原因在于仅靠改写即足以消除文本水印<sup>[4](#ref-4)</sup>。

{{TABLE:watermark}}

### 开源检测器与基准

{{TABLE:detection}}

### 相关资源：含去 AI 味步骤的写作套件

{{TABLE:adjacent}}

## 关于普及程度、检测与水印的证据

**科研文献中的普及程度。** 超额词汇分析表明，2024 年至少 13.5% 的 PubMed 摘要经过 LLM 处理<sup>[1](#ref-1)</sup>（代码：[berenslab/llm-excess-vocab](https://github.com/berenslab/llm-excess-vocab)）。基于分布的估计显示，截至 2024 年 9 月，计算机科学摘要中 22.5% 的句子经过 LLM 修改<sup>[2](#ref-2)</sup>。

**检测及其局限。** 七个常用检测器将超过半数由非英语母语者撰写的托福作文判定为 AI 生成<sup>[3](#ref-3)</sup>。在 DAMAGE 审查中，humanizer 改写使 GPTZero 的召回率从 99.73% 降至 60.04%，DIPPER 改写使 SynthID 检出率从 87.6% 降至 5.4%<sup>[4](#ref-4)</sup>。相比之下，结构级方法对表层编辑表现出更强的鲁棒性：仅凭叙事结构特征即可识别 AI 生成的小说，macro-F1 达 93.2%，且在人工编辑改写文风后依然有效<sup>[5](#ref-5)</sup>；IdeaLens 则依据观点与论证结构而非用词进行检测<sup>[6](#ref-6)</sup>。在同行评审方面，Pangram 估计 ICLR 2026 约 21% 的审稿意见完全由 AI 生成<sup>[7](#ref-7)</sup>。

**水印。** SynthID-Text 在生成阶段通过锦标赛采样嵌入水印，并已在生产规模部署<sup>[8](#ref-8)</sup>；更早的 Kirchenbauer 等人的 green-list 方案在每一步划分词表，并使采样偏向一个伪随机子集<sup>[9](#ref-9)</sup>。

## 新闻与期刊政策

- *Nature* 新闻，2026 年 7 月。['Humanizer' tool can erase signs of AI-written text — alarming scientists](https://www.nature.com/articles/d41586-026-02105-3)<sup>[12](#ref-12)</sup>。
- *The Register*，2026 年 7 月 8 日。[Tool promises to make lazy academics' AI-written papers sound more human](https://www.theregister.com/a/5268460)。
- *TechCrunch*，2025 年 11 月 20 日。[The best guide to spotting AI writing comes from Wikipedia](https://techcrunch.com/2025/11/20/the-best-guide-to-spotting-ai-writing-comes-from-wikipedia/)；原始指南：[Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)。
- 36氪，2026 年 5 月。[论文 AI 检测，正在逼疯这届大学生](https://www.36kr.com/p/3823851041476992)。朱自清《荷塘月色》被测出 62.88% 的 AI 率。
- 央视新闻（光明网转载），2026 年 5 月 22 日。[毕业论文将检测AIGC率，检测标准科学吗？](https://m.gmw.cn/2026-05/22/content_1304466247.htm) 国内高校设定的 AIGC 率门槛为 15%–40%。
- **期刊政策。** Nature Portfolio 允许 AI 辅助的语言润色，但更大程度的写作支持须予披露<sup>[10](#ref-10)</sup>；*Science* 系列期刊要求披露所用工具、版本及完整提示词<sup>[11](#ref-11)</sup>。

## 展望与待解问题

目前仍有三个问题悬而未决。其一，本合集中尚无任何工具被证明能在保留内容的前提下改变第④层得分；鉴于检测器测量的正是改写模型自身的输出分布，基于 LLM 的改写能否做到这一点仍无定论。其二，随着结构级检测器日趋成熟<sup>[5](#ref-5),[6](#ref-6)</sup>，第②层编辑带来的优势可能逐渐减弱，关注点将转向论证与证据本身。其三，已有记录显示检测器对非英语母语者<sup>[3](#ref-3)</sup>及经典人类文本存在假阳性，这使得在评估中采用固定检测阈值的做法值得商榷。涵盖多文本、多语言与多检测器的系统性基准测试将有助于回答上述问题。

## 使用原则

这些工具应用于使本人的文字更加清晰，而非掩盖 AI 的参与。改写后须逐一核对所有数字与结论，因为部分 Skill 会遗漏事实或使主张超出证据。无论检测结果如何，作者均应遵守相应期刊、资助方或所在机构的披露要求。

## 参考文献

1. <a name="ref-1"></a>Kobak, D., González-Márquez, R., Horvát, E.-Á. & Lause, J. Delving into LLM-assisted writing in biomedical publications through excess vocabulary. *Sci. Adv.* **11**, eadt3813 (2025). [doi:10.1126/sciadv.adt3813](https://doi.org/10.1126/sciadv.adt3813) · [arXiv](https://arxiv.org/abs/2406.07016)
   - *依据词频变化估计 PubMed 中 LLM 处理比例的下限。*
2. <a name="ref-2"></a>Liang, W. et al. Quantifying large language model usage in scientific papers. *Nat. Hum. Behav.* (2025). [doi:10.1038/s41562-025-02273-8](https://doi.org/10.1038/s41562-025-02273-8) · [PDF](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf)
3. <a name="ref-3"></a>Liang, W., Yuksekgonul, M., Mao, Y., Wu, E. & Zou, J. GPT detectors are biased against non-native English writers. *Patterns* **4**, 100779 (2023). [doi:10.1016/j.patter.2023.100779](https://doi.org/10.1016/j.patter.2023.100779)
   - *系统记录了检测器对非英语母语写作者的假阳性。*
4. <a name="ref-4"></a>Masrour, E., Emi, B. & Spero, M. DAMAGE: detecting adversarially modified AI generated text. Preprint at [arXiv:2501.03437](https://arxiv.org/abs/2501.03437) (2025).
   - *迄今对 humanizer 最直接的审查：涵盖质量下降、检测器召回率与水印消除。*
5. <a name="ref-5"></a>Russell et al. StoryScope. Preprint at [arXiv:2604.03136](https://arxiv.org/abs/2604.03136) (2026).
6. <a name="ref-6"></a>IdeaLens（马里兰大学）. Preprint at [arXiv:2610.06778](https://arxiv.org/abs/2610.06778) (2026).
7. <a name="ref-7"></a>Pangram 对 ICLR 2026 AI 生成审稿意见的估计，据 *Nature* 新闻报道，并见 [arXiv:2602.00319](https://arxiv.org/abs/2602.00319) 引用 (2026).
8. <a name="ref-8"></a>Dathathri, S. et al. Scalable watermarking for identifying large language model outputs. *Nature* **634**, 818–823 (2024). [doi:10.1038/s41586-024-08025-4](https://doi.org/10.1038/s41586-024-08025-4) · [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11499265/)
9. <a name="ref-9"></a>Kirchenbauer, J. et al. A watermark for large language models. In *Proc. 40th International Conference on Machine Learning* (ICML, 2023). [代码](https://github.com/jwkirchenbauer/lm-watermarking)
10. <a name="ref-10"></a>Nature Portfolio. Artificial intelligence (AI). Editorial policies. <https://www.nature.com/nature-portfolio/editorial-policies/ai>
11. <a name="ref-11"></a>*Science* 系列期刊 AI 披露政策，据 *Times Higher Education* 报道。<https://www.timeshighereducation.com/node/729880>
12. <a name="ref-12"></a>'Humanizer' tool can erase signs of AI-written text — alarming scientists. *Nature*（新闻，2026 年 7 月）. <https://www.nature.com/articles/d41586-026-02105-3>

## 参与贡献

如需新增或修改条目，请编辑 [data/entries.yaml](data/entries.yaml)，运行 `python scripts/build_readme.py`，然后提交 pull request。收录标准与分层方法见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

[CC0 1.0](LICENSE)。所链接项目沿用各自的许可协议。

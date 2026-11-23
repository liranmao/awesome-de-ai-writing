# Awesome De-AI Writing｜去 AI 味工具综述

## 实操建议

| 你要写的 | 推荐 | 避开 |
|---|---|---|
| 英文论文、基金本子 | [academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer)（数字、引用不动，检查动词是否强于证据）；通用润色用 [humanizer](https://github.com/blader/humanizer) | [stop-slop](https://github.com/hardikpandya/stop-slop)（禁被动语态）、[anti-defensive-writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)（会删不利结果） |
| 中文理工论文 | [Humanizer-zh](https://github.com/op7418/Humanizer-zh)（保留学术文体的正式程度、被动句和术语） | 降 AIGC 类工具 |
| 中文文科论文 | 引文多用 [说人话](https://github.com/MrGeDiao/shuorenhua)（默认不动引语和文献），想整体改用 [Humanizer-zh](https://github.com/op7418/Humanizer-zh)；再用 [writing-dna-skill](https://github.com/larashero3-dotcom/writing-dna-skill) 喂入自己以前的文章，保留个人笔调；社科投刊可加 [Awesome-Journal-Skills](https://github.com/brycewang-stanford/Awesome-Journal-Skills) | [human-writing](https://github.com/KKKKhazix/human-writing)（偏口语化）、[anti-defensive-writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)（按实验指标设计） |
| 公众号、博客、社媒 | 中文 [human-writing](https://github.com/KKKKhazix/human-writing)，英文 [humanizer](https://github.com/blader/humanizer) | — |
| 小说、叙事 | [sepia](https://github.com/Nanako0129/sepia) | — |
| 想从源头避免 | [talk-normal](https://github.com/hexiecs/talk-normal)（一段系统提示词） | — |

用之前记住四件事：

1. **先想清楚目的。** 这些工具能让读者读得舒服，但基本过不了 GPTZero、知网这类检测器，原因见图 1。
2. **有旧文先喂样本。** humanizer、academic-humanizer、writing-dna-skill 都支持参考你自己的文章，改出来更像你。
3. **改完逐条核对。** 数字、引文原文、限定词（「可能」「suggest」）、不利结果，有没有被改动或删掉。
4. **按投稿方要求披露 AI 使用**，与检测结果无关。

***本 GitHub repo 包含了 {{SKILLS}} 个 >1000 star 的去 AI 味 Skill。***

[English](README.md) · 星数截至 {{ASOF}}，每周自动更新

<p align="center"><img src="assets/fig1_zh.svg" alt="图 1：去 AI 味工具作用于哪一层，以及各层由谁识别" width="100%"></p>

**图 1｜去 AI 味工具作用于哪一层，以及各层由谁识别。** 中间为文本可能携带机器痕迹的四个层次；左侧为按时机分组的干预方式，曲线粗细与作用于该层的收录工具数成正比；右侧为各层的主要识别者。红色标注示意层次错位：多数改写 Skill 作用于第②层，而商业检测器测量的是第④层。

## 表 1｜按原理分类

{{LAYER_TABLE}}

## 表 2｜按目的分类

{{PURPOSE_TABLE}}

⚠️ 以绕过检测为卖点的工具，效果均为作者自述、未经验证，列出仅为完整起见，不予推荐。无论使用哪种工具，改写后均须逐一核对数字与结论，并按投稿方要求披露 AI 使用。

## 参与贡献

如需新增或修改条目，请编辑 [data/entries.yaml](data/entries.yaml)（表格行的文字说明见 [data/tables.yaml](data/tables.yaml)），运行 `python scripts/build_readme.py`，然后提交 pull request。收录标准与分层方法见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

[CC0 1.0](LICENSE)。所链接项目沿用各自的许可协议。

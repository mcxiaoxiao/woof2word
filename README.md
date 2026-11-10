<div align="center">

# 🐾 dog2text

### The Canine Rosetta Stone
**How Far Are We from Translating What Dogs Say?**

*A survey of cross-species communication decoding in the age of foundation models.*

[![Paper](https://img.shields.io/badge/paper-25%20pages-E8A87C?style=flat-square)](paper/main.pdf)
[![License](https://img.shields.io/badge/license-MIT-8FB996?style=flat-square)](LICENSE)
[![Page](https://img.shields.io/badge/site-cute%20%F0%9F%90%B6-9CC5E8?style=flat-square)](https://mcxiaoxiao.github.io/dog2text/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-E7A6B0?style=flat-square)](#contributing--参与)

**English** · [中文](#中文)

</div>

---

## The question · 问题

> Can a machine turn a bark into a sentence? Consumer apps already claim
> ">80% accuracy." Landmark projects decode whales, dolphins, and finches.
> So — **how far are we, really, from translating what a dog says?**

This repo holds an open, evidence-bounded **survey** that refuses to answer
with a single number. Instead it gives you a **ruler**.

## The translation ladder · 翻译阶梯

"Translating a dog" is not one capability but five. Our central finding:
**today's systems live on Rung 2, with a foothold on Rung 3.** Everything
above is aspirational or — in the strong sense — *ill-posed*.

| Rung | Capability | Status |
|:---:|---|---|
| 1 | **Signal** — detection & segmentation | ✅ solved |
| 2 | **Affect** — emotion / arousal class | ✅ shipping (this is what "translators" really do) |
| 3 | **Intent** — goal + context inference | 🌱 emerging (soundboards) |
| 4 | **Reference** — symbol → object | ❓ unproven |
| 5 | **Dialogue** — open-ended exchange  possibly ill-posed |

The dashed line between Rung 2 and 3 is the **semantic gap**: a dog's natural
signal has no recursive, generative grammar to translate. More compute won't
fix a category error.

<p align="center">
  <img src="paper/figures/fig1_ladder.png" alt="The translation ladder" width="80%">
</p>

## What's inside · 内容

```
dog2text/
├── paper/
│   ├── main.tex            # the survey (LaTeX, TikZ figures)
│   ├── main.pdf            # compiled, 25 pages
│   ├── sections/           # 11 sections + bibliography
│   └── figures/            # hero figures (PNG previews)
├── docs/
│   └── index.html          # the cute project page (GitHub Pages)
├── sources/
│   └── search-log.md       # documented searches & dates
├── README.md
├── CITATION.cff
└── LICENSE
```

## The honest answer · 诚实的回答

- **Rungs 1–2:** essentially here. A *calibrated, validated* welfare monitor
  (stress / pain / arousal) is a **2–4 year** horizon. Useful — but not
  "translation."
- **Rung 3:** a foothold. Validated natural-signal intent ≈ **2030+**, once
  the evaluation infrastructure exists.
- **Rungs 4–5:** **no credible timeline.** There may be no language there to
  translate. The Rosetta Stone worked because one decree existed in three
  scripts; for the dog, there may be no decree — only a rich, graded,
  affective life we can learn to *read*, but not to *transcribe*.

## Build the paper · 编译

Requires [Tectonic](https://tectonic-typesetting.github.io/) (self-contained
LaTeX engine):

```bash
cd paper
tectonic main.tex      # → main.pdf
```

## Citation · 引用

```bibtex
@misc{dog2text2026,
  title  = {The Canine Rosetta Stone: How Far Are We from Translating
            What Dogs Say? A Survey},
  author = {The dog2text Project},
  year   = {2026},
  url    = {https://github.com/mcxiaoxiao/dog2text}
}
```

## Contributing · 参与

Corrections, missing references, and **falsification attempts** are welcome
(see §10 of the paper for what would change our mind). Open an issue or PR.
Please keep claims evidence-bounded: label vendor numbers as *claims*, and
peer-reviewed results as *results*.

---

<a name="中文"></a>
## 中文

**我们距离翻译小狗说的话还有多远？** 本仓库是一篇开放、证据有界的**综述**
（25 页），核心工具是一架"翻译阶梯"：把"翻译狗语"拆成五层能力。结论是——
**今天的产品停在第 2 层（情绪分类），少数研究摸到第 3 层（意图）**；再往上
要么尚待证实，要么在严格意义上**是个伪命题**，因为狗的自然信号里并没有
可供翻译的递归生成语法。

- 第 1–2 层（信号 / 情绪）：已经实现，**2–4 年**内可做出经过校准与验证的
  福利监测工具——有用，但不是"翻译"。
- 第 3 层（意图）：已有立足点（说话按钮研究），自然信号的意图验证约 **2030+**。
- 第 4–5 层（指称 / 对话）：**没有可信时间表**。罗塞塔石碑之所以成功，是因为
  同一份诏书有三种文字；而狗那里也许根本没有"诏书"，只有一段丰富、渐变、
  以情绪为主的生命，我们可以学着**读懂**，却无法**转写**成句子。

论文用 `tectonic main.tex` 编译；主页在 `docs/index.html`；检索记录在
`sources/search-log.md`。欢迎纠错与"证伪"。

<div align="center">

🐶 *Read the dog, don't transcribe it.* 🐾

</div>
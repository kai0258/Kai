# Deep Research

A production-grade research operating system built on top of [hv-analysis](https://github.com/KKKKhazix/khazix-skills). Adds source auditing, quality scoring, tool layering, and delivery standards to the horizontal-vertical analysis framework.

**hv-analysis is the methodology. Deep Research is the execution system.**

[中文文档](#中文文档)

---

## What it does

Deep Research turns a research request into a scored, audited report through a six-stage pipeline that cannot be skipped:

```
Request Parsing → Source Collection → Source Audit → Report Writing → Quality Review → Delivery
```

The key differentiator is **Stage 3 (Source Audit)** — before writing begins, the agent must verify that information is sufficient, balanced, and traceable. If the core narrative chain has gaps, it must search again. If it still can't find the information, it marks it as "information unavailable" rather than fabricating.

## Quick start

### Option A: Agent install prompt (recommended)

We provide a ready-to-use prompt template: [`AGENT_INSTALL_PROMPT.md`](AGENT_INSTALL_PROMPT.md). Copy its content, paste it to your AI Agent (Claude Code, Hermes, Codex, etc.), and the Agent will:

1. Clone the repo and install the skill
2. Scan all placeholder values across 4 files
3. Ask you for your archive path and research region
4. Fill in the values for you

If you just want the short version, paste this:

```
请帮我安装 Deep Research Skill。从 https://github.com/kai0258/Kai.git 克隆仓库，把 deep-research 目录复制到你的 skills 目录下。完成后扫描 SKILL.md、references/irsp.md、references/audit-checklist.md、references/source-audit-methodology.md 中的占位符（搜索 [your-archive-directory] 和 [用户自定义]），把需要我填写的位置整理成清单告诉我，然后问我存档路径和研究领域，帮我填进去。
```

### Option B: Shell script

The [`install.sh`](install.sh) script auto-detects `~/.hermes/skills/` and `~/.claude/skills/`, installs to both, and prints a checklist of all placeholder values you need to fill in.

One-liner (download and run):

```bash
bash <(curl -sL https://raw.githubusercontent.com/kai0258/Kai/main/deep-research/install.sh)
```

Or clone first, then run locally:

```bash
git clone --depth 1 https://github.com/kai0258/Kai.git /tmp/kai-skills
bash /tmp/kai-skills/deep-research/install.sh
# or specify a custom target:
bash /tmp/kai-skills/deep-research/install.sh /path/to/your/skills/
```

### Option C: Manual install

Copy the `deep-research` directory into your agent's skills folder:

```
~/.hermes/skills/          # Hermes
~/.claude/skills/          # Claude Code
```

**Required:**
- Agent environment (Claude Code, Hermes, Codex, etc.)
- Web search capability (WebSearch / WebFetch)

**Recommended:**
- firecrawl (search + scrape)
- exa (semantic search)

Without firecrawl/exa the skill degrades — still usable, but experience is not as smooth as hv-analysis with basic WebSearch.

## ⚠️ Configuration required before first use

This skill ships with **placeholder values** that you must customize for your own research context. Read this section before running your first research.

### 1. Banned source list (critical)

The IRSP protocol excludes state-controlled propaganda outlets from being used as evidence. However, **the list of banned sources is intentionally left blank** — you need to define it yourself based on your region and research domain.

**Where to configure:**

| File | What to fill in |
|------|-----------------|
| `references/irsp.md` | The example list in the "Core Rules" section (line ~20) |
| `references/audit-checklist.md` | The `[用户自定义的受控媒体名单]` placeholder in the sources section check |
| `references/source-audit-methodology.md` | The `banned = [...]` list in the review script template |

**How to fill in:** Add the names and domains of state-controlled media outlets relevant to your research. For example, if you research topics involving Russia, you might add RT and TASS. If you research topics involving a different region, add the relevant outlets from that region.

### 2. Archive path

In `SKILL.md`, the delivery path is set to `[your-archive-directory]`. Replace it with your actual path where completed reports should be saved.

### 3. Tool configuration

The tool layering strategy references specific tools (firecrawl, exa, academic-research MCP). If you don't have all of them, the skill will degrade gracefully — but you should know which tools you have available before starting.

### Why we don't ship a pre-filled list

Different users research different regions. A researcher studying East Asian politics needs a different banned-source list than someone studying European affairs. Shipping a pre-filled list would either be incomplete (missing your region) or overreaching (including regions you never research). **You know your own research context better than we do.**

## Core features

### Source Quality Protocol (IRSP)

Four-tier credibility grading (A/B/C/D) with specific rules:

- State-controlled propaganda outlets are excluded outright
- Academic sources prioritized over media; media over blogs
- Wikipedia and other tertiary sources allowed for navigation, but not as sole evidence for key conclusions
- Conflicting high-quality sources are presented side-by-side, not forced into false consensus

### 13-item scoring matrix (100-point scale, 90 to pass)

| # | Criterion | Points |
|---|-----------|--------|
| 1 | Narrative quality (vertical) | 15 |
| 2 | Key node expansion | 10 |
| 3 | Decision logic reconstruction | 10 |
| 4 | Horizontal scene judgment (A/B/C) | 5 |
| 5 | Horizontal analysis depth | 15 |
| 6 | Cross-axis originality | 10 |
| 7 | Future scenario logic | 5 |
| 8 | Source quality | 10 |
| 9 | Information balance | 5 |
| 10 | Writing style | 5 |
| 11 | No prohibited patterns | 5 |
| 12 | Length compliance | 5 |
| 13 | Critical fact traceability | 5 |

**Hard vetoes** (immediate rejection): fabricated information, textbook-style opening ("In today's rapidly evolving AI era...").

**Soft vetoes** (section locked to minimum score): 2+ instances of filler phrases, buzzwords, or empty adjectives.

### Tool layering strategy

| Layer | Tools | When |
|-------|-------|------|
| Core search | firecrawl_search, exa_web_search | Always |
| Deep extraction | firecrawl_scrape, firecrawl_extract, firecrawl_agent | Known URLs, complex navigation |
| Academic boost | academic-research MCP, my-research MCP | Cross-verification, DOI lookup |

When a layer is unavailable (API limits, MCP not installed), the agent falls back gracefully instead of failing.

### Depth levels

| Level | Words | Use case |
|-------|-------|----------|
| L1 Quick scan | 3,000–5,000 | Single clear object |
| L2 Standard | 10,000–15,000 | Medium complexity |
| L3 Deep | 15,000–30,000 | Long history, high controversy |

## File structure

```
deep-research/
├── SKILL.md                           # Main file — full six-stage pipeline
├── references/
│   ├── irsp.md                        # Source screening protocol + tertiary source policy
│   ├── quality.md                     # 13-item scoring matrix with rubrics
│   ├── writing.md                     # Style guide (rhythm, narrative drive, cultural elevation)
│   ├── audit-checklist.md             # Four-layer audit checklist for batch review
│   └── source-audit-methodology.md    # Source audit methodology + review script template
└── scripts/
    └── write_report.py                # Segmented write tool for long reports
```

## Background

hv-analysis defines the horizontal-vertical framework: vertical axis for temporal depth, horizontal axis for contemporary breadth, cross-axis for original insight. The framework works well. But hv-analysis is a writing guide — it tells you what a good report looks like, not how to guarantee quality.

Deep Research inherits the analysis framework entirely, then adds execution-level safeguards:

| Dimension | hv-analysis | Deep Research |
|-----------|-------------|---------------|
| Positioning | Writing guide | Research operating system |
| Pipeline | 5 steps | 6 steps (+ source audit) |
| Sources | "Primary over secondary" | A/B/C/D grading + cross-verification |
| Quality | 14 checkboxes | 13-item scoring matrix, 100-point scale |
| Veto | None | Hard veto + soft veto |
| Tools | WebSearch/WebFetch | Three-layer strategy |
| Length | Fixed 10K–30K words | L1/L2/L3 adaptive |
| Weight | Lightweight, web-friendly | Heavy, agent-only |

### When to use which

Use hv-analysis when you need a quick overview and don't require strict source auditing. It's lighter, faster, easier to get started.

Use Deep Research when you need a report that can withstand scrutiny — key facts backed by sources, both sides of controversies covered, no AI-speak filler or fabrication. It's heavier and slower, but the quality floor is higher.

They're not in conflict. Think of Deep Research as the production-environment version of hv-analysis.

## Limitations

1. **Heavier.** SKILL.md + 5 references + 1 script = more tokens on first load.
2. **Slower.** Two extra stages (source audit + quality review) add execution time.
3. **Tool-dependent.** Designed for firecrawl/exa; without them, degradation is noticeable.
4. **Limited validation.** 69 reports produced so far across products, companies, concepts, people, and historical events. Not a large-scale controlled study.

## Related projects

- [hv-analysis](https://github.com/KKKKhazix/khazix-skills) — Horizontal-vertical analysis methodology

---

## 中文文档

### 这是什么

横纵分析法深度研究的执行系统。在 hv-analysis 的基础上，加装来源审计、质检复查、工具分层等模块。

**hv-analysis 是方法论，Deep Research 是执行系统。**

### 适用场景

需要一份经得起推敲的研究报告时使用——关键事实有来源支撑、正反面声音都有覆盖、不会出现AI味的套话和编造。

适合研究：产品、公司、概念、人物、历史事件、技术范式。

### 六阶段流水线

```
需求解析 → 信息采集 → 信息审计 → 报告写作 → 质检复查 → 交付存档
```

每一步不可跳过。关键区别在第三步「信息审计」——动笔之前确保信息是够的。

### 信息源质量协议（IRSP）

- **来源可信度分级**：A/B/C/D四级
- **受政权控制的宣传机构一律排除**
- **多源印证规则**：识别循环印证、通稿分发等陷阱
- **三级来源规范**：Wikipedia等可用于导航，但不得作为关键结论的唯一依据
- **来源冲突处理**：高质量来源意见不一致时，并列呈现、评估证据强度，不强行调和

### 13项评分矩阵

满分100分，90分及格。每项有分值、评分标准和常见扣分点。

**硬否决（直接不交付）：** 编造信息、教科书开头

**软否决（该项锁死最低分）：** 2处以上套话、2处以上踩雷词、空洞形容词

### v2 新增特性

相比初版，当前版本新增：

- **Trigger Decision Rules**：基于意图的触发规则
- **Critical Fact Definition**：关键事实的明确界定
- **Source Ledger**：来源台账
- **Information Gap Handling**：信息不足时的标准化处理
- **Comparison Mode Selection**：横轴分析前的A/B/C场景判断
- **Core Findings**：报告开头新增核心结论摘要
- **Scope and Boundaries**：覆盖范围与已知局限
- **Research Date**：研究日期标注
- **三级来源规范**：百科类来源的使用流程和限制
- **来源冲突处理协议**
- **四层审查清单**：版本一致性、信息源合规、模糊引用、三级来源依赖
- **来源审查方法**：含审查脚本模板
- **文化升维**：连接到更大的文化/哲学/历史参照物
- **回环呼应**：开头埋的钩子在结尾callback

### 文件结构

```
deep-research/
├── SKILL.md                           # 主文件，完整的六阶段流程
├── references/
│   ├── irsp.md                        # 信息源筛查协议（含三级来源规范、来源冲突处理）
│   ├── quality.md                     # 13项评分矩阵详细标准
│   ├── writing.md                     # 写作风格指南（含文化升维、回环呼应）
│   ├── audit-checklist.md             # 四层审查清单（批量质检用）
│   └── source-audit-methodology.md    # 来源质量审查方法（含审查脚本模板）
└── scripts/
    └── write_report.py                # 长报告分段写入脚本
```

### 安装

#### 方式一：给 Agent 一句话搞定（推荐）

我们提供了一个现成的安装提示词模板：[`AGENT_INSTALL_PROMPT.md`](AGENT_INSTALL_PROMPT.md)。复制内容发给你的 Agent，它会自动完成安装并引导你配置所有占位符。

如果你不想打开文件，直接复制这段话发给 Agent 也行：

```
请帮我安装 Deep Research Skill。从 https://github.com/kai0258/Kai.git 克隆仓库，把 deep-research 目录复制到你的 skills 目录下。完成后扫描 SKILL.md、references/irsp.md、references/audit-checklist.md、references/source-audit-methodology.md 中的占位符（搜索 [your-archive-directory] 和 [用户自定义]），把需要我填写的位置整理成清单告诉我，然后问我存档路径和研究领域，帮我填进去。
```

#### 方式二：Shell 脚本

[`install.sh`](install.sh) 脚本会自动检测 `~/.hermes/skills/` 和 `~/.claude/skills/`，安装到两个位置，并打印需要填写的占位符清单。

一行命令：

```bash
bash <(curl -sL https://raw.githubusercontent.com/kai0258/Kai/main/deep-research/install.sh)
```

或克隆后本地运行：

```bash
git clone --depth 1 https://github.com/kai0258/Kai.git /tmp/kai-skills
bash /tmp/kai-skills/deep-research/install.sh
# 指定自定义安装路径：
bash /tmp/kai-skills/deep-research/install.sh /path/to/your/skills/
```

#### 方式三：手动安装

将 `deep-research` 目录放到你的skills目录下：

- Hermes: `~/.hermes/skills/`
- Claude Code: `~/.claude/skills/`

**必须：** Agent环境 + 联网搜索能力

**推荐：** firecrawl + exa

### ⚠️ 使用前必须配置

本 skill 附带的是**占位值**，你需要根据自己的研究领域自行填入。

#### 1. 受控媒体名单（最重要）

IRSP 协议会排除受政权控制的宣传机构，但**具体排除哪些媒体，需要你自己定义**。

| 文件 | 需要填入的位置 |
|------|---------------|
| `references/irsp.md` | 核心铁律章节中的示例列表 |
| `references/audit-checklist.md` | 来源章节检查中的 `[用户自定义的受控媒体名单]` |
| `references/source-audit-methodology.md` | 审查脚本模板中的 `banned = [...]` 列表 |

填入你研究领域涉及的受控媒体名称和域名。不同用户研究不同地区，没有通用答案。

#### 2. 存档路径

`SKILL.md` 中的存档路径是 `[your-archive-directory]`，替换为你的实际路径。

#### 3. 工具配置

工具分层策略引用了 firecrawl、exa、academic-research MCP 等工具。没有全部装齐也能用，但会退化。开始研究前确认你有哪些工具可用。

### 局限

1. **更重**：SKILL.md + 5个references + 1个scripts，首次加载token更多
2. **更慢**：多了信息审计和质检复查两个环节
3. **更挑工具**：没有firecrawl/exa时会退化
4. **验证规模有限**：已产出69篇报告，但不是大规模对照实验

### 什么时候用 hv-analysis，什么时候用 Deep Research

快速了解一个对象 → hv-analysis（轻量、快速）

需要经得起推敲的报告 → Deep Research（重、慢、但质量下限更高）

两者不冲突。Deep Research 的分析框架完全继承自 hv-analysis，只是在执行层面加了保障措施。

---

## License

MIT

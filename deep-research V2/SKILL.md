---
name: deep-research
description: |
  Six-stage deep research methodology with horizontal-vertical analysis, IRSP source screening, quality scoring (90+), and archival standards. Key additions: intent-based trigger rules, critical fact traceability, source ledger, information gap handling, Core Findings summary, Scope & Boundaries, Research Date, Comparison Mode Selection (A/B/C), Conflicting Evidence Protocol. Use for systematic deep research on products, companies, concepts, people, movements, ideas. Trigger phrases: "deep research", "横纵分析", "深度研究", "研究一下", "帮我分析", "做个研究", "调研一下", "竞品分析", "analyze this". 横纵分析、深度研究、研究一下、帮我分析、做个研究、调研一下、竞品分析、deep research、analyze this. Do NOT trigger for: simple definitions, translation, short factual answers, title generation, simple summarization, formatting requests, blog writing (use khazix-writer). Trigger by intent, not keywords.
---

# 深度研究法（Deep Research）

> 一套从信息获取到质量交付的完整研究操作系统。分析框架沿用横纵分析法，但增加了信息源筛查（IRSP）、信息审计、质量评分、交付存档四个关键环节。

## 核心理念

研究的价值取决于三件事：**信息是否可靠**、**分析是否深入**、**判断是否独到**。大多数研究失败在第一步——用了不可靠的信息源，后面再精妙的分析也是空中楼阁。

本Skill的六阶段流水线确保每一步都不可跳过：

```
需求解析 → 信息采集 → 信息审计 → 报告写作 → 质检复查 → 交付存档
```

---

## Trigger Decision Rules

Deep Research should be triggered based primarily on user intent rather than keyword matching.

Trigger when the user requests:

- Research
- Investigation
- Comparative analysis
- Historical reconstruction
- Competitive landscape analysis
- Trend analysis
- Policy analysis
- Controversy analysis
- Long-form synthesis

Do NOT trigger when the request is primarily:

- Definition lookup
- Translation
- Short factual answer
- Title generation
- Simple summarization
- Formatting requests

---

## Critical Fact Definition

A statement is considered a critical fact if it contains:

- Dates
- Numbers
- Statistics
- Rankings
- Cause-and-effect claims
- Comparative conclusions
- Claims about impact
- Claims about responsibility
- Claims under active dispute

All critical facts must be traceable to evidence.

---

## 阶段一：需求解析

拿到用户的研究请求后，快速确认以下要素。如果用户已经说得足够明确（比如「帮我研究一下Hermes Agent」），不需要追问，直接开始。

1. **研究对象**：具体的产品名/公司名/概念名/人名
2. **类型判断**：产品 | 公司 | 概念 | 人物 | 运动/事件 | 其他
3. **敏感度评估**：是否涉及政治/意识形态/历史争议性话题 → 如是，激活信息源筛查协议（IRSP，详见 references/irsp.md）
4. **深度等级**（根据对象复杂度和用户暗示自动判断）：
   - **L1 速览**（3000-5000字）：Exa搜索为主，适合单一明确对象
   - **L2 标准**（10000-15000字）：Exa+Firecrawl，适合中等复杂度
   - **L3 深度**（15000-30000字）：全工具链，适合历史长、争议大的对象

---

## 阶段二：信息采集

### 工具分层策略

**第一层（核心搜索，必用）**：
- `firecrawl_search`：最强大的网页搜索工具，优先使用
- `exa_web_search_exa`：语义搜索，发现firecrawl可能遗漏的深层内容

**第二层（深度提取，按需）**：
- `firecrawl_scrape`：已知具体URL时，提取页面完整内容
- `firecrawl_extract`：从多个URL中提取结构化信息
- `firecrawl_agent`：自主研究agent，适合需要多步导航的复杂信息获取

**第三层（学术增强，网络可用时启用）**：
- `academic-research` MCP：`smart_search`多源学术搜索、`validate_citations`验证DOI、`open_access`找免费PDF
- `my-research` MCP：`search_openalex`搜索250M+学术目录、`download_paper`下载论文全文

> **注意**：第三层工具依赖外部API，可能因网络环境不可用。此时完全依赖第一、二层，不形成依赖风险。学术MCP的价值在于：关键事实的交叉验证、核心论文的DOI确认、引用计数查证。

### 并行搜索策略

每个研究对象至少执行四轮搜索，覆盖不同维度：

- **轮1 — 纵向**：对象名 + "history" / "origin" / "development" / "timeline"
- **轮2 — 横向**：对象名 + "compared to" / "alternative" / "vs" / "competitor"
- **轮3 — 平衡**：对象名 + "criticism" / "controversy" / "problem" / "failure"
- **轮4 — 补充**：根据前三轮发现的缺口，针对性搜索

### 信息源优先级

一手来源优于二手来源，多个媒体引用同一个错误会造成循环印证假象：

| 信息类型 | 一手来源 |
|---------|---------|
| 产品/技术决策 | 官方文档、GitHub、创始人原文 |
| 商业/财务数据 | 官方公告、工商/SEC文件、权威数据库 |
| 用户口碑 | GitHub Issues、Reddit、社区讨论 |
| 学术/理论 | 学术期刊论文、会议论文集、原始著作 |
| 行业分析 | 权威媒体原创报道（非转载） |
| 历史事件 | 一手史料、口述历史、学术传记 |

### 来源台账（Source Ledger）

For each source, maintain an internal source ledger with the following fields:

- Source Name
- URL
- Publication Date
- Access Date
- Evidence Supported
- Source Tier (A/B/C/D per IRSP)
- Potential Conflict of Interest

The ledger is an internal audit artifact and should not necessarily appear in the final report. It serves as the traceability backbone for all critical facts.

### 信息充分性自检（采集完成后立即执行）

- 纵向：能讲出完整故事吗？有没有明显的时间断层？
- 横向：竞品/同类列表完整吗？每个竞品的信息够做对比吗？
- 来源：关键事实有可靠来源支撑吗？有没有只靠单一来源就下判断的？
- 平衡：听到了支持者的声音，也有批评者的声音吗？

信息不够就再补搜。不要凑合。

### 兜底规则

实际执行中经常遇到搜索无结果、网页无法访问、API限流等情况。处理原则：

- 如果某个方向的搜索多次无果，诚实记录为「该方向信息暂缺」，不要编造
- 优先保证已有信息的深度，而不是为了覆盖所有方向而降低信息质量
- 已获取的一手来源如果充分，不必为了"看起来全面"而强行拼凑低质量二手源
- 搜索工具不可用时（如API 401、限流），切换到备用工具或手动构造URL用抓取工具直接提取

### 信息缺口处理（Information Gap Handling）

If evidence is insufficient:

1. Attempt targeted follow-up search.
2. If evidence remains unavailable:
   - explicitly acknowledge the gap
   - avoid speculation
   - reduce confidence level accordingly

Never fabricate missing information.

---

## 阶段三：信息审计

> 这是本Skill与原横纵分析法最关键的差异。信息采集完成后、动笔写作前，必须执行一次独立审计。

### 审计清单

**完整性审计**：
- □ 纵向时间线是否覆盖了从起源到当下的完整弧线？
- □ 每个关键节点至少有2个独立来源支撑？
- □ 横向对比的主要对象是否都有足够信息做深入分析？

**平衡性审计**：
- □ 是否同时找到了正面评价和负面评价/批评？
- □ 有没有「房间里的大象」——显而易见但搜索结果回避的问题？
- □ 研究对象的失败、弱点、争议有没有被充分记录？

**可靠性审计**（如涉及敏感话题，执行IRSP，详见 references/irsp.md）：
- □ A/B级来源占比是否超过60%？
- □ 有没有过度依赖单一来源？
- □ 关键争议性事实有没有交叉验证？

### 审计输出

记录以下信息（内部使用，不交付给用户）：
1. **信息缺口清单**：哪些问题搜不到或信息不足 → 驱动补搜
2. **可靠性风险清单**：哪些事实的来源不够强 → 写作时标注不确定性
3. **补搜计划**（如有）：用什么关键词补搜

### 补搜决策

- 如果核心叙事链上有断层 → **必须补搜**，不补搜不进入写作
- 如果某些细节搜不到 → **诚实标注「该信息暂缺」**，绝不编造
- 如果某个竞品/对比方信息不足 → **减少展开篇幅，或替换为信息更充分的对象**

---

## 阶段四：报告写作

### 框架选择

根据研究对象类型，自动适配横纵分析法的具体变体：

| 对象类型 | 纵轴重点 | 横轴重点 |
|---------|---------|---------|
| 产品 | 版本迭代、技术路线、用户增长 | 功能对比、性能、定价、用户体验 |
| 公司 | 创始团队、融资、战略转向 | 商业模式、市场份额、组织架构 |
| 概念 | 概念起源、理论争论、流变 | 相近概念对比、适用场景、阵营论证 |
| 人物 | 个人经历、关键决策、成长曲线 | 同领域人物对比、风格、路线差异 |
| 运动/事件 | 起源、关键节点、阶段划分 | 相关运动对比、策略、影响力 |

### 报告结构模板

```
# [研究对象名称]

> Research Date: YYYY-MM-DD | 所属领域：XXX | 研究对象类型：XXX

## Core Findings

[3–5 concise, evidence-backed conclusions. Each conclusion should be 1–3 sentences. Avoid narrative detail. The reader should understand the main takeaways within 30 seconds of opening the report.]

## Scope and Boundaries

This section must state:
- What is covered
- What is not covered
- Known limitations

All conclusions are bounded by information available before the research date.

## 一、一句话定义
[用一句话说清楚这个东西是什么]

一句话定义的质量标准：
  - 好的定义应该同时回答：它是什么、为谁服务、核心价值/核心特征是什么
  - 不要写成百科词条式的定义，要写成让人想继续往下读的钩子
  - 不要在定义里提前剧透后面的判断和结论
  - 人物类：可以用"一个……的人，通过……，做到了/造成了……"的句式
  - 事件类：可以用"一场发生在……的……，最终导致了……"的句式

## 二、纵向分析：[有画面感的副标题]
[完整的纵向叙事，占全文60%]

### 2.1 [阶段标题]（时间范围）
### 2.2 ...
### 2.N 阶段划分总结（表格）
### 2.N+1 路径依赖分析
### 2.N+2 叙事线索

## 三、横向分析：[有画面感的副标题]
[横向对比分析，占全文25%]

### 3.1 竞品/同类场景判断（A/B/C）

Comparison Mode Selection:

- **Mode A**: No meaningful direct competitors exist.
- **Mode B**: A small number of competitors exist but differ substantially.
- **Mode C**: Multiple comparable competitors exist.

The report must explain why a mode was selected.

### 3.2 逐一深入对比
### 3.3 维度对比矩阵（表格）
### 3.4 竞争格局/定位判断

## 四、横纵交汇洞察
[交叉分析和未来推演，占全文15%]

### 4.1 历史如何塑造了当下的位置
### 4.2 竞品的纵向对比
### 4.3 优势与劣势的历史根源
### 4.4 未来推演（三个剧本）

## 五、信息来源
[编号列表，含URL和访问时间]

## 六、方法论说明
[1-2句话说明横纵分析法来源]
```

### 写作风格

详见 references/writing.md。核心要点：

- **叙事驱动**，不是罗列驱动。有起承转转合。
- **敢下判断**，但每个判断必须有事实支撑。
- **行内引用铁律**：每个关键事实必须标注来源，格式为自然嵌入（据XXX报道/记载/研究）
- **用人话写**：避免咨询公司套话，用具体细节代替概括陈述

### 信息源铁律

详见 references/irsp.md。核心规则：
- 受政权控制的宣传机构来源一律排除（用户可自定义受控媒体名单）
- 英文学术/媒体来源优先
- 无法确定中立性时排除该来源
- 搜不到的信息诚实标注「该信息暂缺」，绝不编造

### 信息源常见陷阱（2026-05-30 审查总结）

**Wikipedia 不可作为主信源**：Wikipedia 可用于事实核查和初步了解，但正文叙事不能建立在"据Wikipedia记载"之上。超过5处Wikipedia行内引用 = 需重写。

**平台 ≠ 学术来源**：华艺线上图书馆、知网/CNKI、爱思想等是文献检索平台，不是学术信源。引用时必须追溯到原始论文的作者、期刊名、年份。"据华艺线上图书馆" = 不可接受。

**"历史提及" vs "信源引用"**：正文中提到"某媒体发表了XXX社论"是历史事实描述（可接受）；"据某受控媒体报道"是把宣传机构当信源（不可接受）。判断标准：受控媒体名在"据...记载"的主语位置 = 违规。

**模糊引用一律扣分**："据历史学家""据多位学者""据研究""据媒体"——没有具体人名/期刊/年份的引用 = 来源质量扣分项。详见 references/source-audit-methodology.md。

### 输出格式

**默认Markdown**。仅在用户明确要求时生成PDF。这是用户偏好，必须记住。

---

## 阶段五：质检复查

报告初稿完成后，对照以下评分矩阵逐项打分。详见 references/quality.md。

### 评分矩阵（满分100）

| # | 检查项 | 分值 | 评分标准 |
|---|--------|------|---------|
| 1 | 纵轴叙事质量 | 15 | 因果逻辑、叙事弧线、细节密度 |
| 2 | 关键节点展开度 | 10 | 每个节点有事件+背景+原因+结果 |
| 3 | 决策逻辑还原 | 10 | 不只说「发生了什么」，还说「为什么这么选」 |
| 4 | 横轴场景判断 | 5 | A/B/C判断正确 |
| 5 | 横轴分析深度 | 15 | 每个主要对比方至少1500字展开 |
| 6 | 横纵交汇原创性 | 10 | 产出新判断，非前文缩写 |
| 7 | 未来推演逻辑 | 5 | 三个剧本各有支撑 |
| 8 | 信息来源质量 | 10 | A/B级>60%，行内引用完整 |
| 9 | 信息平衡性 | 5 | 正反面声音都有 |
| 10 | 写作风格 | 5 | 节奏感、可读性、无AI味 |
| 11 | 无禁区违规 | 5 | 逐条检查绝对禁区 |
| 12 | 篇幅达标 | 5 | 总字数在深度等级目标范围内 |

### 否决机制

**硬否决（直接不交付，必须重写）**：
- 编造信息（搜不到就编、伪造来源、捏造数据）
- 教科书开头（"在当今AI快速发展的时代"、"随着技术的不断进步"）

**软否决（触发后该项锁死最低分，必须修改后重新评分）**：
- 出现2处以上套话（"首先...其次...最后"、"综上所述"、"值得注意的是"）
- 出现2处以上高频踩雷词（"说白了"、"意味着什么？"、"本质上"、"换句话说"）
- 空洞形容词（"赋能"、"抓手"、"打造闭环"）

硬否决优先于总分：即使其他项目满分，触发硬否决仍不交付。

### 复查流程

1. 先检查是否触发硬否决 → 如触发，直接要求重写，不进入打分流程
2. 逐项打分，记录每项扣分原因
3. 总分 ≥ 90：进入交付阶段
4. 总分 < 90：针对最低分项进行第一轮补强，然后重新复查
5. 第一轮补强后仍未达90分：**暂停补强**，输出一份补强方案（列出每项扣分原因、拟采取的具体补强措施、预期提升幅度），交由用户审核确认
6. 用户确认方案后，按方案执行第二轮补强，然后重新复查
7. 上限：最多补强2轮（第一轮自动执行 + 第二轮需用户审核）。如2轮后仍未达标，诚实告知用户当前版本的不足之处

### 绝对禁区（逐条检查）

以下AI味标记无论什么文体都要避免：
- 套话：「首先...其次...最后」「综上所述」「值得注意的是」「不难发现」
- 空洞形容词：「赋能」「抓手」「打造闭环」
- 教科书开头：「在当今XX快速发展的时代」「随着XX的不断进步」
- 高频踩雷词：「说白了」「意味着什么？」「这意味着」「本质上」「换句话说」「不可否认」
- 编造场景：搜不到就诚实标注，绝不编造

---

## 阶段六：交付存档

### 交付物

- `[研究对象]_横纵分析报告.md`（默认）
- `[研究对象]_横纵分析报告.pdf`（仅用户明确要求时，使用 hv-analysis skill 的 `scripts/md_to_pdf.py`）

### 存档路径

`[your-archive-directory]`

### 文件命名

- 中文对象：`[对象名]_横纵分析报告.md`
- 英文对象：`[Object_Name]_HV_Analysis.md`

### 末尾必须包含

1. **信息来源**：编号列表，含来源名称、URL（如有）、访问时间
2. **方法论说明**：1-2句话说明横纵分析法来源

---

## 长报告写入工作流（关键）

横纵分析报告通常2-3万字，超出单次 write_file 的高效范围。**必须分段写入**。

### 使用 write_report.py 脚本

本skill内置了 `scripts/write_report.py` 工具脚本，自动处理分段写入和验证：

```bash
# 第一段：创建文件，写入正文（第一至第四部分）
python3 scripts/write_report.py create /path/to/report.md "正文内容..."

# 后续段：追加来源章节
python3 scripts/write_report.py append /path/to/report.md "来源内容..."

# 后续段：追加方法论和附录
python3 scripts/write_report.py append /path/to/report.md "方法论内容..."

# 当内容太长无法作为命令行参数时，先写到临时文件再追加
python3 scripts/write_report.py append-file /path/to/report.md /tmp/segment.md

# 验证文件状态和章节完整性
python3 scripts/write_report.py verify /path/to/report.md
```

### 写入节奏

| 轮次 | 内容 | 模式 |
|------|------|------|
| 第1轮 | 第一至第四部分（正文） | create |
| 第2轮 | 第五部分（信息来源） | append |
| 第3轮 | 第六部分（方法论）+ 附录 | append |

**每段控制在 5000 字以内**。如果某个部分超过 5000 字，拆成多次 append。

### 关键注意事项

- **来源章节单独一轮写入**——这是最容易被截断的部分。审核数据显示，来源章节长度与报告总字数不完全成正比，说明写到后半段时输出空间已不足。
- **写完后用 verify 验证**——确认所有章节完整、文件未截断。
- **禁止**：echo、heredoc、cat、python -c 写长文件。

---

## 参考文件

以下文件按需加载，不要一次性全部读取：

- **references/irsp.md** — 信息源筛查协议（Information Resource Screening Protocol）。涉及政治/意识形态/历史争议话题时必须读取。
- **references/quality.md** — 质检评分矩阵的详细版，含每项的具体评分标准和常见扣分点。进入阶段五时读取。
- **references/writing.md** — 写作风格指南的完整版，含节奏感、叙事驱动、文化升维等详细说明。进入阶段四时读取。
- **references/audit-checklist.md** — 研究报告批量质量审查清单，含四层检查（版本一致性、信息源合规、模糊引用、三级来源依赖）。用于审查已有报告或阶段五复查时参考。
- **references/source-audit-methodology.md** — 信息源质量审查方法。批量审查已有报告时读取。含"历史提及 vs 信源引用"判断规则、问题模式分级、审查脚本模板。

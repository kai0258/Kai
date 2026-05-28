# Kai's AI Skills

个人调教的 AI Agent Skills 集合。每个 skill 都是长期使用中逐步打磨出来的，不是模板生成的。

---

## Deep Research Skill

横纵分析法深度研究的执行系统。在 [hv-analysis](https://github.com/KKKKhazix/khazix-skills) 的基础上，加装来源审计、质检复查、工具分层等模块。

**一句话说清楚两者的关系：hv-analysis是方法论，Deep Research是执行系统。**

### 背景

hv-analysis skill（横纵分析法）来自 [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)。

Deep Research是用横纵分析法分析课题时，逐步改造出的更适合实际使用的分析方法。

hv-analysis定义了「横纵分析法」这个研究框架——纵轴追时间深度，横轴追同期广度，最后交汇出判断。这个框架本身没有问题，效果很好。但hv-analysis作为一个skill，它更像是一个「写作指南」而不是「研究操作系统」。它告诉你报告应该长什么样，但没有告诉你怎么保证报告的质量。

Deep Research在hv-analysis的基础上，做了几个关键改造。

### 适用场景

需要一份经得起推敲的研究报告时使用——关键事实有来源支撑、正反面声音都有覆盖、不会出现AI味的套话和编造。

适合研究：产品、公司、概念、人物、历史事件、技术范式。

### 与hv-analysis的核心区别

| 维度 | hv-analysis | Deep Research |
|------|-------------|---------------|
| 定位 | 写作指南 | 研究操作系统 |
| 流程 | 5步 | 6步（多了信息审计） |
| 信息源 | "一手优于二手" | A/B/C/D四级分级 + 多源印证 |
| 质检 | 14个checkbox | 12项评分矩阵，100分制，90分及格 |
| 否决机制 | 无 | 硬否决（编造/教科书开头）+ 软否决（套话/踩雷词） |
| 工具 | WebSearch/WebFetch | 三层分层策略 |
| 篇幅 | 固定1-3万字 | L1/L2/L3三档 |
| 重量 | 轻量，网页端可用 | 重量级，仅限Agent环境 |

### 六阶段流水线

```
需求解析 → 信息采集 → 信息审计 → 报告写作 → 质检复查 → 交付存档
```

每一步不可跳过。关键区别在第三步「信息审计」——动笔之前确保信息是够的。

#### 信息审计做了什么？

信息采集完成后，agent必须先执行一次独立审计：
- 纵向时间线有没有断层？
- 每个关键节点有没有2个以上独立来源支撑？
- 正反面声音都有吗？

核心叙事链有断层就必须补搜，补不了才标注「该信息暂缺」。这一步确保了「动笔之前信息是够的」。

### 信息源质量协议（IRQP）

hv-analysis有一条简单的规则：「一手来源优于二手来源」。这当然对，但远远不够。

Deep Research内置了一套完整的信息源质量协议：

- **来源可信度分级**：A/B/C/D四级
- **多源印证规则**：识别循环印证、通稿分发、匿名知情人士等陷阱
- **时效性规则**：技术类6个月过期，商业类以最近财年为准
- **立场平衡规则**：争议话题必须引用不同立场的来源

这套协议的价值不在于「排除坏来源」，而在于「建立判断来源好坏的思维框架」。

### 12项评分矩阵 + 否决机制

hv-analysis有一个质检清单，14个checkbox，逐条打勾。问题是：checkbox只能告诉你「有没有做」，不能告诉你「做得好不好」。

Deep Research用12项评分矩阵替代了checkbox，满分100，90分及格。每项都有分值、评分标准和常见扣分点。

#### 否决机制

**硬否决（直接不交付）：**
- 编造信息
- 教科书开头（「在当今AI快速发展的时代」）

**软否决（该项锁死最低分）：**
- 2处以上套话
- 2处以上踩雷词
- 空洞形容词

硬否决优先于总分——即使其他项目满分，触发硬否决仍不交付。

### 工具分层策略

hv-analysis告诉agent「必须联网搜索」，然后给了几个工具名。Deep Research把搜索工具分成了三层：

- **第一层（核心搜索）**：firecrawl_search、exa_web_search
- **第二层（深度提取）**：firecrawl_scrape、firecrawl_extract、firecrawl_agent
- **第三层（学术增强）**：academic-research MCP、my-research MCP

分层的意义在于：当某一层工具不可用时（比如API限流、MCP没装），agent知道该退到哪一层，而不是直接报错或放弃。

### 深度等级

| 等级 | 字数 | 适用场景 |
|------|------|----------|
| L1 速览 | 3,000-5,000 | 单一明确对象，以Exa搜索为主 |
| L2 标准 | 10,000-15,000 | 中等复杂度，Exa+Firecrawl |
| L3 深度 | 15,000-30,000 | 历史长、争议大的对象，全工具链 |

这意味着研究「Hermes Agent」和研究「女权主义运动史」不应该用同一套流程。

### 写作风格和禁区

两者在写作风格上的要求高度一致，但Deep Research把「绝对禁区」从写作建议升级为了质检标准。

hv-analysis说「不要写套话」，Deep Research说「写套话扣分，写多了不交付」。

前者是建议，后者是纪律。

### 文件结构

```
deep-research/
├── SKILL.md                    # 主文件，完整的六阶段流程
├── references/
│   ├── quality.md              # 12项评分矩阵详细标准
│   ├── writing.md              # 写作风格指南
│   └── irsp.md                 # 信息源筛查协议
└── scripts/
    ├── write_report.py         # 长报告分段写入脚本
    └── md_to_pdf.py            # Markdown转PDF脚本
```

### 使用要求

**必须：**
- Agent环境（Claude Code、Hermes、Codex等）
- 联网搜索能力（WebSearch/WebFetch）

**推荐：**
- firecrawl（搜索 + 抓取）
- exa（语义搜索）

没有firecrawl/exa时会退化，体验不如直接用hv-analysis。

### 安装

将 `deep-research` 目录放到你的skills目录下：

- Hermes: `~/.hermes/skills/`
- Claude Code: `~/.claude/skills/`

### Deep Research的局限

说了这么多优点，也要诚实讲局限：

1. **更重**。hv-analysis是一个轻量级skill，文件小、流程短、上手快。Deep Research有SKILL.md + 3个references + 2个scripts，首次加载token更多。
2. **更慢**。多了信息审计和质检复查两个环节，执行时间更长。
3. **更挑工具**。Deep Research的工具分层策略假设你有firecrawl和exa，如果没有，退化后的体验不如hv-analysis直接用WebSearch/WebFetch流畅。
4. **验证规模有限**。hv-analysis来自Khazix的开源项目，经过了多次迭代；Deep Research是我在实际使用中逐步改造的，目前已经产出69篇横纵分析报告，覆盖产品、公司、概念、人物、历史事件等多种类型，累计消耗大几亿token。

### 什么时候用哪个

如果你只是想快速了解一个产品或概念，不需要严格的来源审计和质检流程，hv-analysis足够了。它轻量、快速、上手容易。

如果你需要一份经得起推敲的研究报告——关键事实有来源支撑、正反面声音都有覆盖、不会出现AI味的套话和编造——用Deep Research。它更重、更慢，但质量下限更高。

两者并不冲突。Deep Research的分析框架完全继承自hv-analysis，只是在执行层面加了更多保障措施。你可以把Deep Research理解为hv-analysis的「生产环境版本」。

### 相关项目

- [hv-analysis](https://github.com/KKKKhazix/khazix-skills) - 横纵分析法方法论

---

## Teacher Agent Universal v3

一个可迁移的长期私人教师系统——不是"会讲课的 AI"，而是一个能长期带学、持续诊断、动态调整教学策略的 Teacher Agent。

**核心思想：用文件仓库代替 AI 的短期记忆，用课程状态文件代替一次性聊天，用长期教学协议代替普通问答。**

### 它是什么

- 长期私人教师，不是问答机器人
- 课程设计者 + 学习诊断者 + 节奏控制者
- 基于 Bloom 掌握学习法，未掌握则不推进
- 支持 Book-Locked 教学——锁定一本书/文件夹作为唯一知识来源

### 核心特性

#### 1. Book-Locked Teaching（v3 核心）

指定一本书、一个 PDF、或整个文件夹作为唯一教学来源：

```
/booktopic 福柯导读
资料路径：D:\Books\Foucault.pdf
```

Agent 只能根据指定资料教学，禁止偷渡外部知识。资料没写的内容会明确说"指定材料未覆盖此点"。

适合：研究生、法律、哲学、政治学、社科、理论书、技术文档。

#### 2. 六种课程模式动态切换

| 模式 | 用途 |
|------|------|
| Normal Lesson | 正常推进 |
| Practice Lesson | 现场陪练 |
| Remedial Lesson | 修补知识裂缝 |
| Branch Lesson | 兴趣深挖 |
| Checkpoint Lesson | 阶段检测 |
| Book-Locked Lesson | 书籍锁定教学 |

#### 3. 黑匣子审计机制

每轮记录：为什么推进、为什么不矫正、真实风险、教学法选择依据。防止"看起来在教，其实在乱推"。

#### 4. Bloom 掌握学习

持续判断用户处于 Remember → Understand → Apply → Analyze → Evaluate → Create 的哪一层，未掌握则强制矫正，不机械推进。

### 仓库结构

```
TeacherAgent_Universal_v3/
├── _SYSTEM/          # Agent 的"宪法层"——教师身份、执行链、反懒规则
├── _TEMPLATE/        # 新课题初始化模板
├── IDENTITY.md
└── SOUL.md
```

课题目录示例（一个仓库 = 一个长期学习宇宙）：

```
TeacherAgent_Universal_v3/
├── 传播学基础/
├── 法理学/
├── 福柯导读/
├── Python基础/
└── 政治传播学/
```

每个课题目录包含：`learning_state.md`、`pedagogical_log.md`、`pedagogical_blackbox.md`、`lessons/`、`checkpoints/`、`source_scope.md`。

### 快速开始

#### Step 1：部署人格

将 `人格设定.txt` 的内容粘贴到 AI 平台的 System Prompt / Persona / Character / Identity 位置。

#### Step 2：告知仓库路径

```
Teacher Agent 仓库位于：D:\你的路径\TeacherAgent_Universal_v3
```

#### Step 3：确认进入 Teacher 模式

首次启动后，让它读取 `_SYSTEM` 并汇报规则摘要。如果它开始闲聊，说明没启动成功。

#### Step 4：创建新课题

```
/newtopic 传播学基础
```

或 Book-Locked 模式：

```
/booktopic 福柯导读
资料路径：D:\Books\Foucault.pdf
```

### Book-Locked 正确行为

✅ "这本书这里的意思其实是在说……"
✅ "作者这里隐含了一个前提……"
✅ "指定资料没有解释这一点。"

❌ "我补充一下外部学界观点……"
❌ "虽然书里没写，但其实……"

### 推荐运行环境

| 环境 | 推荐度 | 原因 |
|------|--------|------|
| Qclaw | ⭐⭐⭐⭐⭐ | 文件读写能力强 |
| Hermes | ⭐⭐⭐⭐ | Agent 框架，文件操作完整 |
| Claude Desktop | ⭐⭐⭐⭐ | 长上下文支持 |
| OpenAI Agent | ⭐⭐⭐ | 基本可用 |
| 普通网页聊天 | ⭐ | 缺少文件持久化，效果差 |

Teacher Agent 本质是文件仓库驱动系统，文件读写能力越强，效果越好。

---

## 许可

MIT

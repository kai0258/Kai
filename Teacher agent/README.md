# Teacher Agent Universal v3

一个可迁移的长期私人教师系统——不是"会讲课的 AI"，而是一个能长期带学、持续诊断、动态调整教学策略的 Teacher Agent。

核心思想：用**文件仓库**代替 AI 的短期记忆，用**课程状态文件**代替一次性聊天，用**长期教学协议**代替普通问答。

## 它是什么

- 长期私人教师，不是问答机器人
- 课程设计者 + 学习诊断者 + 节奏控制者
- 基于 Bloom 掌握学习法，未掌握则不推进
- 支持 Book-Locked 教学——锁定一本书/文件夹作为唯一知识来源

## 核心特性

### 1. Book-Locked Teaching（v3 核心）

指定一本书、一个 PDF、或整个文件夹作为唯一教学来源：

```
/booktopic 福柯导读
资料路径：D:\Books\Foucault.pdf
```

Agent 只能根据指定资料教学，禁止偷渡外部知识。资料没写的内容会明确说"指定材料未覆盖此点"。

适合：研究生、法律、哲学、政治学、社科、理论书、技术文档。

### 2. 六种课程模式动态切换

| 模式 | 用途 |
|------|------|
| Normal Lesson | 正常推进 |
| Practice Lesson | 现场陪练 |
| Remedial Lesson | 修补知识裂缝 |
| Branch Lesson | 兴趣深挖 |
| Checkpoint Lesson | 阶段检测 |
| Book-Locked Lesson | 书籍锁定教学 |

### 3. 黑匣子审计机制

每轮记录：为什么推进、为什么不矫正、真实风险、教学法选择依据。防止"看起来在教，其实在乱推"。

### 4. Bloom 掌握学习

持续判断用户处于 Remember → Understand → Apply → Analyze → Evaluate → Create 的哪一层，未掌握则强制矫正，不机械推进。

## 仓库结构

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

## 快速开始

### Step 1：部署人格

将 `人格设定.txt` 的内容粘贴到 AI 平台的 System Prompt / Persona / Character / Identity 位置。

### Step 2：告知仓库路径

```
Teacher Agent 仓库位于：D:\你的路径\TeacherAgent_Universal_v3
```

### Step 3：确认进入 Teacher 模式

首次启动后，让它读取 `_SYSTEM` 并汇报规则摘要。如果它开始闲聊，说明没启动成功。

### Step 4：创建新课题

```
/newtopic 传播学基础
```

或 Book-Locked 模式：

```
/booktopic 福柯导读
资料路径：D:\Books\Foucault.pdf
```

## Book-Locked 正确行为

✅ "这本书这里的意思其实是在说……"
✅ "作者这里隐含了一个前提……"
✅ "指定资料没有解释这一点。"

❌ "我补充一下外部学界观点……"
❌ "虽然书里没写，但其实……"

## 推荐运行环境

| 环境 | 推荐度 | 原因 |
|------|--------|------|
| Qclaw | ⭐⭐⭐⭐⭐ | 文件读写能力强 |
| Hermes | ⭐⭐⭐⭐ | Agent 框架，文件操作完整 |
| Claude Desktop | ⭐⭐⭐⭐ | 长上下文支持 |
| OpenAI Agent | ⭐⭐⭐ | 基本可用 |
| 普通网页聊天 | ⭐ | 缺少文件持久化，效果差 |

Teacher Agent 本质是文件仓库驱动系统，文件读写能力越强，效果越好。

## 包含文件

- `人格设定.txt` — Agent 初始人格（System Prompt）
- `使用手册.txt` — 完整部署与使用手册
- `TeacherAgent_Universal_v3.zip` — 仓库模板压缩包

## License

MIT

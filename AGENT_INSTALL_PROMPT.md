# Agent Install Prompt
#
# 把下面这段话发给你的 AI Agent（Claude Code、Hermes、Codex 等），
# Agent 会自动完成安装并提醒你需要配置的内容。
#
# 用法：复制下方内容，粘贴给你的 Agent。

---

请帮我安装 Deep Research Skill。

步骤：

1. 从 GitHub 克隆仓库：
   git clone --depth 1 https://github.com/kai0258/Kai.git /tmp/deep-research-repo

2. 把 deep-research 目录复制到你的 skills 目录：
   - Hermes: ~/.hermes/skills/deep-research/
   - Claude Code: ~/.claude/skills/deep-research/
   如果 skills 目录不存在，先创建。

3. 复制完成后，扫描以下三个文件中的占位符，列出所有需要我填写的位置：
   - SKILL.md — 搜索 [your-archive-directory]
   - references/irsp.md — 搜索"用户可根据所在地区自行补充"
   - references/audit-checklist.md — 搜索 [用户自定义的受控媒体名单]
   - references/source-audit-methodology.md — 搜索 [用户自定义受控媒体名单]

4. 把扫描结果整理成清单告诉我，格式：
   文件 | 行号 | 占位符内容 | 需要填入什么

5. 然后问我：你的存档路径是什么？你研究的领域涉及哪些地区？

6. 我回答后，帮我把值填进去。

7. 清理临时文件（/tmp/deep-research-repo）。

# Kai

Open-source skills, workflows, and research systems for AI agents.

Kai is a collection of production-ready agent capabilities designed for Claude Code, Hermes, Codex, and other AI agent environments. The repository focuses on three areas:

* Research and knowledge work
* Multi-agent orchestration
* Long-term learning and task execution

The goal is simple: help AI agents produce more reliable, structured, and reproducible work.

---

## Featured Projects

### Deep Research

A research operating system for AI agents.

Deep Research transforms a research request into a structured report through a mandatory six-stage pipeline:

```
Request Parsing → Source Collection → Source Audit → Report Writing → Quality Review → Delivery
```

Key capabilities:

* Source quality grading (IRSP protocol)
* Evidence traceability
* Multi-source verification
* Structured quality review
* Adaptive report depth (L1/L2/L3)
* Tool-layering support (Web Search, Firecrawl, Exa, Academic Research)

Built on top of [hv-analysis](https://github.com/KKKKhazix/khazix-skills) methodology.

- **Location:** [`Deep Research skill/`](Deep%20Research%20skill/) (original) / [`deep-research V2/`](deep-research%20V2/) (updated)
- **Install:** `git clone` this repo, copy `deep-research/` to `~/.hermes/skills/` or `~/.claude/skills/`. Or run `bash install.sh`. Or paste `AGENT_INSTALL_PROMPT.md` to your Agent.

---

### Teacher Agent

A long-term adaptive teaching framework.

Instead of acting as a lecturer, Teacher Agent behaves as a curriculum designer and learning coach.

Key capabilities:

* Mastery-based progression (Bloom's taxonomy)
* Learning-gap diagnosis
* Book-locked study mode
* Multi-stage course design
* Persistent learning records
* Black-box audit log

- **Location:** [`Teacher agent/`](Teacher%20agent/)
- **Install:** Paste `人格设定.txt` into your AI platform's system prompt. Point it at a folder.

---


## Repository Philosophy

Many AI-agent projects focus on generating outputs.

Kai focuses on improving the process behind those outputs.

The repository explores how agents can:

* Research more reliably
* Coordinate more effectively
* Learn more systematically
* Deliver more reproducible results

---

## Validation

Deep Research has produced 199 reports across multiple research domains.

```
History & Historical Analysis ............ 72
Public Institutions & Governance ......... 45
Biographical Research .................... 14
Comparative Systems ...................... 24
Technology & Society ..................... 10
Social & Economic Structure .............. 20
Ideas & Intellectual History ............. 14+
```

Typical output characteristics:

* 10,000–20,000 characters
* Source Ledger
* Scope & Boundaries
* Research Date
* Core Findings
* IRSP source grading
* Evidence traceability

---

## Related Projects

* [Task OS](https://github.com/kai0258/Task-os) — file-based task operating system and orchestration for AI agents
* [hv-analysis](https://github.com/KKKKhazix/khazix-skills) — horizontal-vertical analysis methodology

---

## License

[MIT](LICENSE)


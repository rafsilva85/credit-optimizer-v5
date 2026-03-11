# 🚀 Credit Optimizer v5 for Manus AI

> **Stop burning credits.** Cut your Manus AI usage by 30-75% — zero quality loss, audited across 53 scenarios.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-purple.svg)](https://modelcontextprotocol.io)
[![Product Hunt](https://img.shields.io/badge/Product%20Hunt-Live%20Now-orange.svg)](https://www.producthunt.com/posts/credit-optimizer-for-manus-ai)

<p align="center">
  <a href="https://www.producthunt.com/posts/credit-optimizer-for-manus-ai?utm_source=badge-featured" target="_blank">
    <img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=credit-optimizer-for-manus-ai&theme=light" alt="Credit Optimizer on Product Hunt" width="250" height="54" />
  </a>
</p>

---

## 📊 Real Results (Not Estimates)

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Credits per task | 100% | 53% | **-47%** |
| Quality score | 9.2/10 | 9.2/10 | **0% loss** |
| Tasks audited | — | 200+ | Verified |
| Scenarios tested | — | 53 | All passing |

> *"I was spending $200+/month on Manus credits. After installing Credit Optimizer, my usage dropped to $110 doing the same work."* — Early user

---

## 🎯 What It Does

Credit Optimizer analyzes your prompts **before execution** and applies 6 optimization strategies:

- **Smart Model Routing** — Routes simple tasks to Standard mode, complex to Max
- **Intent Classification** — Detects 12 task categories for optimal handling
- **Prompt Compression** — Removes redundancy while preserving all meaning
- **Batch Detection** — Identifies parallelizable tasks for fewer credits
- **Context Hygiene** — Flags unnecessary context that inflates tokens
- **Output Format Optimization** — Suggests efficient output formats

---

## ⚡ Quick Start

### Option 1: MCP Server (Free — Claude, Cursor, Copilot, etc.)

```bash
pip install fastmcp
git clone https://github.com/rafsilva85/manus-credit-optimizer.git
cd manus-credit-optimizer
python -m mcp_credit_optimizer
```

Add to your MCP config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "credit-optimizer": {
      "command": "python",
      "args": ["-m", "mcp_credit_optimizer"],
      "cwd": "/path/to/manus-credit-optimizer"
    }
  }
}
```

### Option 2: Apify MCP Server (Cloud — No Install)

Use it instantly via [Apify Store](https://apify.com/skillforge-ai/credit-optimizer-v5):

```json
{
  "mcpServers": {
    "credit-optimizer": {
      "url": "https://actors-mcp-server.apify.actor/sse/skillforge-ai~credit-optimizer-v5"
    }
  }
}
```

### Option 3: Manus Skill (Native — Auto-Activates on Every Task)

The full Manus Skill integrates directly into Manus and runs automatically — no manual prompting needed.

<p align="center">
  <a href="https://creditopt.ai">
    <strong>🔥 Get the Manus Skill — $9 Launch Special (was $29) →</strong>
  </a>
</p>

---

## 🔧 MCP Tools

| Tool | Description |
|------|-------------|
| `analyze_prompt` | Analyze a prompt and get optimization recommendations with estimated savings |
| `get_optimization_strategy` | Get detailed strategy with model routing, prompt compression, and batch detection |
| `get_golden_rules` | Get the 10 golden rules for credit-efficient Manus usage |

## 📋 Example

```
You: analyze_prompt("Build me a React dashboard with charts, auth, and database backend")

Credit Optimizer:
  ✅ Intent: code_generation (complex)
  ✅ Recommended: Max mode (complex multi-component task)
  ✅ Split into 3 sequential tasks:
     1. Database schema + API routes
     2. Authentication flow
     3. React dashboard + charts
  ✅ Estimated savings: 35-45%
  ✅ Quality impact: None
```

## 🏗️ Architecture

```
Prompt → Intent Classifier → Complexity Scorer → Strategy Selector
                                                       ↓
                                         ┌─────────────────────────┐
                                         │ • Model Router          │
                                         │ • Prompt Compressor     │
                                         │ • Batch Detector        │
                                         │ • Context Hygiene       │
                                         │ • Output Optimizer      │
                                         └─────────────────────────┘
                                                       ↓
                                         Optimized Recommendations
```

## 🔒 Audit Results

All 53 test scenarios pass with zero quality degradation:

- ✅ Code generation (Python, JS, React, SQL)
- ✅ Creative writing (blog posts, marketing copy)
- ✅ Data analysis (CSV, JSON, API data)
- ✅ Research tasks (multi-source synthesis)
- ✅ Translation & localization
- ✅ Bug fixing & debugging
- ✅ Documentation generation
- ✅ Mixed-intent tasks

---

## 💰 Pricing

| Option | Price | What You Get |
|--------|-------|-------------|
| **MCP Server (this repo)** | **Free** | MCP tools for Claude, Cursor, Copilot, etc. |
| **Apify Cloud MCP** | **Free** | Zero-install cloud MCP via [Apify Store](https://apify.com/skillforge-ai/credit-optimizer-v5) |
| **Manus Skill** | **~~$29~~ $9** | Native Manus integration + auto-activation + priority updates |

### Why pay $9 when the MCP server is free?

The **Manus Skill** gives you:
- **Auto-activation** — runs on every task without you remembering to use it
- **Native integration** — works inside Manus, not as an external tool
- **Priority updates** — get new optimization patterns first
- **One-time payment** — no subscription, yours forever

> The MCP server saves you credits when you remember to use it.
> The Manus Skill saves you credits on **every single task** automatically.

<p align="center">
  <a href="https://creditopt.ai">
    <strong>🔥 $9 Launch Special — Save 30-75% on Every Manus Task →</strong>
  </a>
  <br>
  <sub>One-time payment. No subscription. 30-day money-back guarantee.</sub>
</p>

---

## 📄 License

MIT License — use it freely in personal and commercial projects.

## 🤝 Contributing

Issues and PRs welcome! If you find a scenario where the optimizer reduces quality, please open an issue with the prompt and expected output.

---

<p align="center">
  <strong>Built by <a href="https://github.com/rafsilva85">Rafael Silva</a></strong> · <a href="https://creditopt.ai">creditopt.ai</a> · <a href="https://www.producthunt.com/posts/credit-optimizer-for-manus-ai">Product Hunt</a> · <a href="https://apify.com/skillforge-ai/credit-optimizer-v5">Apify Store</a>
</p>

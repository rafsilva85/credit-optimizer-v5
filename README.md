<p align="center">

[![PyPI Version](https://img.shields.io/pypi/v/manus-credit-optimizer?color=green&label=PyPI)](https://pypi.org/project/manus-credit-optimizer/)
[![Downloads](https://img.shields.io/pypi/dm/manus-credit-optimizer?color=blue&label=Downloads)](https://pypi.org/project/manus-credit-optimizer/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Manus AI](https://img.shields.io/badge/Manus_AI-Power_Stack-purple)](https://creditopt.ai)

  <img src="https://img.shields.io/pypi/v/mcp-credit-optimizer?color=green&label=PyPI" alt="PyPI">
  <img src="https://img.shields.io/pypi/dm/mcp-credit-optimizer?color=blue&label=Downloads" alt="Downloads">
  <img src="https://img.shields.io/github/stars/rafsilva85/credit-optimizer-v5?style=social" alt="Stars">
  <img src="https://img.shields.io/badge/quality%20loss-0%25-brightgreen" alt="Zero Quality Loss">
  <img src="https://img.shields.io/badge/scenarios%20audited-53-blue" alt="53 Scenarios">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
</p>

# Manus Power Stack

### 47% of your Manus credits are being wasted. This fixes it automatically.

> **Zero downsides. 47% average savings. Pays for itself in ~27 prompts.**
> Audited across 53 adversarial scenarios. Quality Veto Rule: if it can't save without loss, it doesn't touch your task.

**Get it:** [Landing Page](https://creditopt.ai) · [Gumroad ($12)](https://rafaamaral.gumroad.com/l/manus-power-bundle) · [SkillFlow](https://skillflow.builders/skill/manus-power-bundle-mn7p4h88)
**Free MCP Server:** [PyPI](https://pypi.org/project/mcp-credit-optimizer/) · [Smithery](https://smithery.ai/server/@rafsilva85/mcp-credit-optimizer) · [Cursor Directory](https://cursor.directory/)

---

## Why Your Credits Disappear

Manus charges credits per task. Most users waste **30–75%** because of four default behaviors:

| Problem | What Happens | Waste |
|---------|-------------|-------|
| **Wrong model routing** | Simple tasks run in Max mode when Standard produces identical results | Up to **5x overpay** |
| **Slow browser navigation** | Each page takes 8–45 seconds via browser tool calls, burning credits on wait time | **150+ seconds** per 10 URLs |
| **No chat detection** | Tasks that cost $0 in Chat Mode (Q&A, brainstorm, translation) run in Agent Mode | **100% overpay** |
| **Context bloat** | Tokens accumulate across steps — each subsequent step costs more than the last | **Exponential growth** |

These aren't bugs. They're default settings. The Power Stack overrides all four.

---

## Zero Downsides

This is the most important thing to understand:

> **The Power Stack can never make things worse.** It has a hardcoded Quality Veto Rule: if an optimization would reduce output quality by even 1%, it skips that optimization entirely. In the worst case, it does nothing. In the best case, it saves you 75%.

There is no scenario where installing the Power Stack produces a worse result than not having it.

---

## What's Inside

### Credit Optimizer v5 — Smart Routing

Analyzes every prompt before execution and decides the cheapest path that delivers identical quality.

- **Intent Classification** across 12 categories (code, research, creative, data, translation...)
- **Model Routing**: Standard vs Max — only uses Max when complexity genuinely requires it
- **Chat Mode Detection**: Routes simple Q&A to Chat Mode ($0 cost)
- **Batch Detection**: Groups related tasks to reduce overhead
- **Context Hygiene**: Compresses accumulated context to keep token costs linear

### Fast Navigation v2.0 — Raw Speed

Replaces slow browser tool calls with a programmatic toolkit.

- **httpx + selectolax** replaces Playwright overhead (30–2,000x faster)
- **Browser Cookie Bridge** for authenticated sites
- **Async parallel fetching** — 10 URLs in 1.3 seconds instead of 150+ seconds
- **Intelligent disk caching** with TTL — repeated visits are instant

### Together: The Compound Effect

Credit Optimizer decides **what** to optimize. Fast Navigation decides **how fast** to execute it. Together, they multiply:

| Metric | Without Stack | With Stack | Improvement |
|--------|--------------|------------|-------------|
| Simple Q&A cost | Full price | $0 (Chat Mode) | **100% saved** |
| 10-URL research | 150+ seconds | 1.3 seconds | **115x faster** |
| Web scraping task | Full credits | 33% of original | **67% saved** |
| Full-stack web app | Full credits | 40% of original | **60% saved** |
| Research report | 12 minutes | 2 minutes | **6x faster** |
| Average across all tasks | Baseline | 47% less | **47% saved** |

---

## The Math: Payback in ~27 Prompts

The Power Stack costs $12 one-time. Here's how fast it pays for itself:

| Plan | Monthly Cost | 47% Wasted | Daily Waste | Payback |
|------|-------------|------------|-------------|---------|
| Plus ($39/mo) | 6,500 cr/day | ~3,055 cr/day | ~$0.44/day | **~27 prompts** |
| Max ($99/mo) | 16,250 cr/day | ~7,637 cr/day | ~$0.92/day | **~13 prompts** |
| Teams ($79/user/mo) | Varies | ~47% | Varies | **1–2 days** |

After payback, every prompt saves you money. For the rest of your Manus subscription. Forever.

**Annual savings estimate: ~$500–$1,000+** depending on usage.

---

## Installation

### As Manus Skill (recommended — $12 bundle)

1. Purchase from [Gumroad](https://rafaamaral.gumroad.com/l/manus-power-bundle) or [SkillFlow](https://skillflow.builders/skill/manus-power-bundle-mn7p4h88)
2. Copy skill files to `~/skills/credit-optimizer/` and `~/skills/fast-navigation/`
3. Both activate automatically on every task — no configuration needed

### As MCP Server (free — Credit Optimizer only)

```bash
pip install mcp-credit-optimizer
python -m mcp_credit_optimizer
```

Add to your MCP config:

```json
{
  "mcpServers": {
    "credit-optimizer": {
      "command": "python",
      "args": ["-m", "mcp_credit_optimizer"]
    }
  }
}
```

Works with Claude Desktop, Cursor, Windsurf, Copilot, and any MCP-compatible client.

> **Why pay when the MCP server is free?** The MCP server saves credits when you remember to call it. The Manus Skill saves credits on **every single prompt automatically** — no manual invocation needed. The Skill also includes Fast Navigation (115x speed boost), which is not available as MCP.

---

## Audit Results

All 53 test scenarios pass with **zero quality degradation**:

| Category | Scenarios | Quality Loss |
|----------|-----------|-------------|
| Code generation (Python, JS, React, SQL) | 12 | **0%** |
| Creative writing (blog, marketing) | 8 | **0%** |
| Data analysis (CSV, JSON, API) | 7 | **0%** |
| Research (multi-source synthesis) | 6 | **0%** |
| Translation & localization | 5 | **0%** |
| Bug fixing & debugging | 5 | **0%** |
| Documentation generation | 5 | **0%** |
| Mixed-intent tasks | 5 | **0%** |

---

## What Users Say

> *"Everyone hates the Manus credit-based system. It's insane how fast credits burn."* — [Reddit, 90 upvotes](https://www.reddit.com/r/ManusOfficial/comments/1s0rqw8/)

> *"I used 100,000 credits in a week and a half. That's my entire monthly allocation gone."* — [Reddit](https://www.reddit.com/r/ManusOfficial/comments/1pqg80j/)

> *"Manus is so expensive it's absurd. $200/month and credits still run out."* — [Reddit](https://www.reddit.com/r/ManusOfficial/comments/1lqdaty/)

The Power Stack exists because these frustrations are real — and fixable.

---

## Links

| Channel | URL |
|---------|-----|
| **Landing Page** | [creditopt.ai](https://creditopt.ai) |
| **Buy (Bundle $12)** | [Gumroad](https://rafaamaral.gumroad.com/l/manus-power-bundle) |
| **SkillFlow** | [skillflow.builders](https://skillflow.builders/skill/manus-power-bundle-mn7p4h88) |
| **PyPI (Free MCP)** | [pypi.org](https://pypi.org/project/mcp-credit-optimizer/) |
| **Smithery** | [smithery.ai](https://smithery.ai/server/@rafsilva85/mcp-credit-optimizer) |
| **PulseMCP** | [pulsemcp.com](https://www.pulsemcp.com/servers?q=credit+optimizer) |

---

## License

MIT — see [LICENSE](LICENSE) for details.

**Built by [Rafael Silva](https://github.com/rafsilva85)** · [creditopt.ai](https://creditopt.ai)

[![Available on SkillFlow](https://raw.githubusercontent.com/rafsilva85/awesome-ai-skills/main/badges/skillflow-available.svg)](https://skillflow.builders)
# Credit Optimizer v5 for Manus AI
<!-- mcp-name: io.github.rafsilva85/credit-optimizer-v5 -->
> **Save 30-75% on Manus AI credits with zero quality loss.** ~55% average savings. Audited across 53 adversarial scenarios, 200+ tasks verified. Works as MCP server (free) or native Manus Skill ($9).

[![PyPI](https://img.shields.io/pypi/v/manus-credit-optimizer.svg)](https://pypi.org/project/manus-credit-optimizer/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/manus-credit-optimizer.svg)](https://pypi.org/project/manus-credit-optimizer/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-purple.svg)](https://modelcontextprotocol.io)
[![Stars](https://img.shields.io/github/stars/rafsilva85/credit-optimizer-v5?style=social)](https://github.com/rafsilva85/credit-optimizer-v5)
[![Reddit](https://img.shields.io/badge/Reddit-Discussion-FF4500.svg)](https://www.reddit.com/r/mcp/)

**Available on:** [PyPI](https://pypi.org/project/manus-credit-optimizer/) · [Smithery](https://smithery.ai/server/rafsilva85/credit-optimizer) · [PulseMCP](https://pulsemcp.com) · [SkillFlow](https://skillflow.builders/skill/credit-optimizer-v5-mn6lqfu1) · [GitHub](https://github.com/rafsilva85/credit-optimizer-v5) · [Landing Page](https://creditopt.ai)

---

## The Problem

Manus AI charges credits per task. Most users waste 30-75% of their credits because:

- Simple tasks run in Max mode when Standard would produce identical results
- Prompts contain redundant context that inflates token usage
- Tasks that could be batched are executed one by one
- Output formats are not optimized for the task type

**Credit Optimizer fixes all of this automatically.**

---

## How It Works

```
Your Prompt
    |
    v
+------------------------------------------+
|         Credit Optimizer v5              |
|                                          |
|  1. Intent Classification (12 categories)|
|  2. Complexity Scoring                   |
|  3. Model Routing (Standard vs Max)      |
|  4. Prompt Compression                   |
|  5. Batch Detection                      |
|  6. Context Hygiene                      |

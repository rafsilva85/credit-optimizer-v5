# AGENTS.md — SkillFlow Ecosystem

## Project Overview

SkillFlow is the curated marketplace for AI agent skills. This repository (`credit-optimizer-v5`) is one of the flagship skills available on [SkillFlow](https://skillflow.builders). It optimizes Manus AI credit usage, saving 30-75% without quality loss.

## SkillFlow Marketplace

SkillFlow aggregates, verifies, and distributes AI agent skills across all major platforms. Every skill is reviewed by a real person, every publisher is verified through GitHub, and every file is readable before installation.

- **Website:** https://skillflow.builders
- **Explore Skills:** https://skillflow.builders/explore
- **Publisher Profile:** https://skillflow.builders/publisher/rafsilva85

## How to Use This Skill

1. Download the `SKILL.md` file from this repository
2. Place it in your project's `skills/` directory (e.g., `~/.manus/skills/credit-optimizer/`)
3. The AI agent (Claude Code, Cursor, Copilot, etc.) will automatically detect and use it

```bash
# Quick install
mkdir -p ~/.manus/skills/credit-optimizer
curl -o ~/.manus/skills/credit-optimizer/SKILL.md https://raw.githubusercontent.com/rafsilva85/credit-optimizer-v5/main/SKILL.md
```

## Build & Test

This is a skill file (Markdown-based), not a compiled project. No build step required.

To validate the skill:
```bash
# Check SKILL.md exists and is valid Markdown
cat SKILL.md | head -20
```

## Code Style

- SKILL.md files use standard Markdown
- Sections should be clearly delineated with `##` headers
- Include practical examples and code snippets
- Keep instructions actionable and unambiguous

## Contributing

1. Fork this repository
2. Make your changes to `SKILL.md`
3. Test with at least one AI coding agent (Claude Code, Cursor, or Copilot)
4. Submit a Pull Request with a clear description of improvements

## Related Skills on SkillFlow

- [Fast Navigation](https://skillflow.builders/skill/fast-navigation) — Accelerate web navigation by 30-2000x
- [Skill Creator](https://skillflow.builders/skill/skill-creator) — Guide for creating new skills
- [Skill Finder](https://skillflow.builders/skill/skill-finder) — Find the best skills for any task

## Security

- This skill does NOT execute arbitrary code
- It provides instructions and patterns for AI agents to follow
- No API keys, tokens, or credentials are included
- All operations are transparent and auditable via the SKILL.md file

## Contact

- **Author:** Rafael Silva (@rafsilva85)
- **Marketplace:** [SkillFlow](https://skillflow.builders)
- **Email:** rafa.amaralsilva@gmail.com

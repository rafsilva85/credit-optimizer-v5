# Changelog

All notable changes to the Manus Credit Optimizer will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [5.2.2] - 2026-03-26

### Changed
- Updated README with unified messaging across all channels
- Improved server.json description for better MCP directory discovery
- Updated PyPI package description with zero downsides messaging
- Added comprehensive savings table with 7 real-world task scenarios

### Fixed
- Fixed Fast Navigation version reference (v2.0, not v3)

## [5.2.1] - 2026-03-20

### Changed
- Improved strategy matrix with more granular task-type routing
- Enhanced efficiency directives for better context hygiene
- Updated credit savings calculations based on latest Manus pricing

## [5.2.0] - 2026-03-15

### Added
- Quality Veto Rule: optimization NEVER overrides quality (hardcoded)
- Smart Testing strategy: test with 1 item before processing batches
- Chat Detection: routes simple Q&A to free chat (saves 100% on those tasks)
- Section-by-section processing for long content generation
- Context hygiene directives to prevent exponential token growth

### Changed
- Refined Standard vs Max model routing thresholds
- Improved file output detection for automatic file-based delivery

## [5.1.0] - 2026-03-01

### Added
- Fast Navigation v2.0 skill (bundled in Power Stack)
- Programmatic web toolkit replacing slow browser tool calls
- Cookie bridge for authenticated sessions
- Async parallel fetching for multi-URL operations

### Changed
- Rebranded from "Credit Optimizer" to "Power Stack" (bundle)
- Updated pricing to $12 one-time for the complete bundle

## [5.0.0] - 2026-02-15

### Added
- Initial release of Credit Optimizer v5
- Intelligent Standard/Max model routing
- 22-scenario audit with 12 vulnerability fixes
- Strategy matrix for task-type-specific optimization
- Efficiency directives for credit-conscious execution

### Changed
- Complete rewrite from v4 architecture
- New modular skill format compatible with Manus AI platform

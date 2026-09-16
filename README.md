# Cloud Architecture Check

[![Tests](https://github.com/YOUR_USERNAME/cloud-architecture-check/actions/workflows/tests.yml/badge.svg)](https://github.com/YOUR_USERNAME/cloud-architecture-check/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A lightweight, vendor-neutral CLI for reviewing cloud architectures against practical principles shared across modern Well-Architected approaches.

## Why this project exists

Cloud providers publish excellent architecture guidance, but hybrid and multi-cloud teams often need a concise, provider-independent baseline that can be used before mapping decisions to a specific platform.

**Cloud Architecture Check** turns that baseline into an executable assessment. It helps architects and engineering teams identify gaps across five core pillars:

- Security
- Reliability
- Performance Efficiency
- Cost Optimization
- Sustainability

The project is intentionally small and extensible. It can be used in architecture reviews, workshops, proofs of concept, training, and CI/CD experiments.

## Features

- Vendor-neutral practice catalog
- JSON-based assessments
- Per-pillar and overall scoring
- Human-readable findings
- Machine-readable JSON output
- Automated tests
- GitHub Actions CI
- Simple extension model for new practices

## Quick start

Requires Python 3.11+.

```bash
git clone https://github.com/YOUR_USERNAME/cloud-architecture-check.git
cd cloud-architecture-check
python -m cloud_arch_check.cli examples/sample-assessment.json
```

If you prefer an editable install:

```bash
python -m pip install -e .
cloud-architecture-check examples/sample-assessment.json
```

## Example

```text
Cloud Architecture Check
========================
Overall score: 80.0%

Security: 100.0%
Reliability: 75.0%
Performance Efficiency: 75.0%
Cost Optimization: 75.0%
Sustainability: 75.0%

Open findings: 4
```

Use `--json` for machine-readable output:

```bash
cloud-architecture-check examples/sample-assessment.json --json
```

## Assessment format

An assessment is a JSON object whose keys correspond to practice IDs from `practices.json`.

Values are:

- `true` — implemented
- `false` — not implemented
- `null` — not assessed

Example:

```json
{
  "SEC-001": true,
  "SEC-002": false,
  "REL-001": true
}
```

Practices not present in an assessment are treated as not assessed and do not affect the score.

## Current practice catalog

The initial catalog contains practical checks covering identity, encryption, network segmentation, backups, recovery testing, failure isolation, autoscaling, observability, rightsizing, cost allocation, lifecycle policies, carbon-aware choices, and utilization efficiency.

The catalog is deliberately vendor-neutral. Future releases may add mappings to public AWS, Microsoft Azure, and Google Cloud guidance while keeping the core assessment independent of any provider.

## Project structure

```text
.
├── practices.json
├── examples/
│   └── sample-assessment.json
├── src/cloud_arch_check/
│   ├── __init__.py
│   ├── cli.py
│   └── engine.py
├── tests/
│   └── test_engine.py
└── .github/workflows/
    └── tests.yml
```

## Roadmap

- Markdown and HTML reports
- Weighted severity / business criticality
- Custom practice catalogs
- Architecture Decision Record (ADR) integration
- Public mappings to major cloud-provider guidance
- Policy-as-code integrations
- CI/CD quality gates
- Additional examples for multi-region and multi-cloud architectures

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License. See [LICENSE](LICENSE).

## Disclaimer

This is an independent open-source project. It is not affiliated with, endorsed by, or sponsored by Amazon Web Services, Microsoft, or Google.

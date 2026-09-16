from __future__ import annotations

import argparse
import json
from pathlib import Path

from .engine import evaluate, load_json


def default_catalog() -> Path:
    return Path(__file__).resolve().parents[2] / "practices.json"


def render_text(result) -> str:
    score = "N/A" if result.overall_score is None else f"{result.overall_score:.1f}%"
    lines = ["Cloud Architecture Check", "=" * 24, f"Overall score: {score}", ""]

    for pillar, value in result.pillar_scores.items():
        pillar_score = "N/A" if value is None else f"{value:.1f}%"
        lines.append(f"{pillar}: {pillar_score}")

    lines.extend(["", f"Open findings: {len(result.findings)}"])
    for finding in result.findings:
        lines.append(f"- [{finding.practice_id}] {finding.title}")

    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Assess cloud architecture practices from a JSON file.")
    parser.add_argument("assessment", help="Path to assessment JSON")
    parser.add_argument("--catalog", default=str(default_catalog()), help="Path to practice catalog JSON")
    parser.add_argument("--json", action="store_true", dest="json_output", help="Emit machine-readable JSON")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    practices = load_json(args.catalog)
    assessment = load_json(args.assessment)
    result = evaluate(practices, assessment)

    if args.json_output:
        print(json.dumps(result.as_dict(), indent=2))
    else:
        print(render_text(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

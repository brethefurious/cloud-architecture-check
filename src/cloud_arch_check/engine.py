from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
import json


@dataclass(frozen=True)
class Finding:
    practice_id: str
    pillar: str
    title: str
    description: str


@dataclass(frozen=True)
class AssessmentResult:
    overall_score: float | None
    pillar_scores: dict[str, float | None]
    assessed: int
    passed: int
    findings: list[Finding]

    def as_dict(self) -> dict[str, Any]:
        return {
            "overall_score": self.overall_score,
            "pillar_scores": self.pillar_scores,
            "assessed": self.assessed,
            "passed": self.passed,
            "findings": [asdict(item) for item in self.findings],
        }


def load_json(path: str | Path) -> Any:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def evaluate(practices: list[dict[str, str]], assessment: dict[str, bool | None]) -> AssessmentResult:
    practice_ids = {practice["id"] for practice in practices}
    unknown = sorted(set(assessment) - practice_ids)
    if unknown:
        raise ValueError(f"Unknown practice IDs: {', '.join(unknown)}")

    pillar_totals: dict[str, int] = {}
    pillar_passed: dict[str, int] = {}
    findings: list[Finding] = []
    assessed = 0
    passed = 0

    for practice in practices:
        practice_id = practice["id"]
        value = assessment.get(practice_id)
        pillar = practice["pillar"]

        if value is None:
            continue
        if not isinstance(value, bool):
            raise ValueError(f"Assessment value for {practice_id} must be true, false, or null")

        assessed += 1
        pillar_totals[pillar] = pillar_totals.get(pillar, 0) + 1
        pillar_passed.setdefault(pillar, 0)

        if value:
            passed += 1
            pillar_passed[pillar] += 1
        else:
            findings.append(
                Finding(
                    practice_id=practice_id,
                    pillar=pillar,
                    title=practice["title"],
                    description=practice["description"],
                )
            )

    all_pillars = list(dict.fromkeys(practice["pillar"] for practice in practices))
    pillar_scores: dict[str, float | None] = {}
    for pillar in all_pillars:
        total = pillar_totals.get(pillar, 0)
        pillar_scores[pillar] = round((pillar_passed.get(pillar, 0) / total) * 100, 1) if total else None

    overall_score = round((passed / assessed) * 100, 1) if assessed else None
    return AssessmentResult(
        overall_score=overall_score,
        pillar_scores=pillar_scores,
        assessed=assessed,
        passed=passed,
        findings=findings,
    )

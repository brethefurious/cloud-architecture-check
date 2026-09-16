import pytest

from cloud_arch_check.engine import evaluate


PRACTICES = [
    {"id": "SEC-001", "pillar": "Security", "title": "Identity", "description": "Use least privilege"},
    {"id": "SEC-002", "pillar": "Security", "title": "Secrets", "description": "Protect secrets"},
    {"id": "REL-001", "pillar": "Reliability", "title": "Recovery", "description": "Test recovery"},
]


def test_scores_only_assessed_practices():
    result = evaluate(PRACTICES, {"SEC-001": True, "SEC-002": False, "REL-001": None})

    assert result.overall_score == 50.0
    assert result.pillar_scores["Security"] == 50.0
    assert result.pillar_scores["Reliability"] is None
    assert result.assessed == 2
    assert result.passed == 1
    assert [item.practice_id for item in result.findings] == ["SEC-002"]


def test_all_passed():
    result = evaluate(PRACTICES, {"SEC-001": True, "SEC-002": True, "REL-001": True})
    assert result.overall_score == 100.0
    assert result.findings == []


def test_unknown_practice_is_rejected():
    with pytest.raises(ValueError, match="Unknown practice IDs"):
        evaluate(PRACTICES, {"UNKNOWN-001": True})


def test_invalid_value_is_rejected():
    with pytest.raises(ValueError, match="must be true, false, or null"):
        evaluate(PRACTICES, {"SEC-001": "yes"})

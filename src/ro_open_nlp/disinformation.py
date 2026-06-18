from __future__ import annotations

from dataclasses import dataclass

from ro_open_nlp.normalization import normalize_text

ALARM_TERMS = {
    "socant",
    "adevarul ascuns",
    "nu vor sa stii",
    "distribuie urgent",
    "presa tace",
    "fara precedent",
    "miracol",
    "conspiratie",
}


@dataclass(frozen=True)
class LexicalSignal:
    score: float
    matched_terms: list[str]


def lexical_disinformation_signal(text: str) -> LexicalSignal:
    normalized = normalize_text(text, lowercase=True)
    matched = sorted(term for term in ALARM_TERMS if term in normalized)
    score = min(1.0, len(matched) / 3)
    return LexicalSignal(score=score, matched_terms=matched)


def make_disinformation_record(
    record_id: str,
    text: str,
    label: str = "unverified",
    source: str | None = None,
) -> dict[str, object]:
    signal = lexical_disinformation_signal(text)
    return {
        "id": record_id,
        "text": text,
        "label": label,
        "source": source,
        "evidence": [],
        "annotator_notes": (
            f"baseline_lexical_score={signal.score:.2f}; "
            f"termeni={signal.matched_terms}"
        ),
        "lang": "ro",
    }


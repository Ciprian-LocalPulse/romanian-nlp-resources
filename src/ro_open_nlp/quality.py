from __future__ import annotations

from ro_open_nlp.normalization import normalize_text
from ro_open_nlp.privacy import contains_personal_data


def text_quality_score(text: str) -> dict[str, float | bool | int]:
    normalized = normalize_text(text)
    chars = len(normalized)
    letters = sum(ch.isalpha() for ch in normalized)
    digits = sum(ch.isdigit() for ch in normalized)
    ratio_letters = letters / chars if chars else 0.0
    ratio_digits = digits / chars if chars else 0.0
    score = 1.0
    if chars < 20:
        score -= 0.35
    if ratio_letters < 0.55:
        score -= 0.25
    if ratio_digits > 0.25:
        score -= 0.2
    if contains_personal_data(normalized):
        score -= 0.4
    return {
        "chars": chars,
        "letter_ratio": round(ratio_letters, 3),
        "digit_ratio": round(ratio_digits, 3),
        "contains_personal_data": contains_personal_data(normalized),
        "score": max(0.0, round(score, 3)),
    }


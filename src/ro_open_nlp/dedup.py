from __future__ import annotations

from collections.abc import Iterable
from difflib import SequenceMatcher
from hashlib import sha256

from ro_open_nlp.normalization import normalize_text


def stable_hash(text: str) -> str:
    return sha256(normalize_text(text, lowercase=True).encode("utf-8")).hexdigest()


def deduplicate_exact(texts: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for text in texts:
        key = stable_hash(text)
        if key not in seen:
            seen.add(key)
            result.append(text)
    return result


def is_near_duplicate(a: str, b: str, threshold: float = 0.92) -> bool:
    left = normalize_text(a, lowercase=True)
    right = normalize_text(b, lowercase=True)
    return SequenceMatcher(None, left, right).ratio() >= threshold


def deduplicate_fuzzy(texts: Iterable[str], threshold: float = 0.92) -> list[str]:
    result: list[str] = []
    for text in texts:
        if not any(is_near_duplicate(text, existing, threshold) for existing in result):
            result.append(text)
    return result


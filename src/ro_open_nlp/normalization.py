from __future__ import annotations

import re
import unicodedata

ZERO_WIDTH_RE = re.compile("[\u200b\u200c\u200d\ufeff]")
SPACE_RE = re.compile(r"[ \t\r\f\v]+")
MULTI_NEWLINE_RE = re.compile(r"\n{3,}")

QUOTE_MAP = str.maketrans(
    {
        "“": '"',
        "”": '"',
        "„": '"',
        "‟": '"',
        "’": "'",
        "‘": "'",
        "‚": "'",
        "–": "-",
        "—": "-",
        "\u00a0": " ",
    }
)


def normalize_text(text: str, *, lowercase: bool = False) -> str:
    """Normalizeaza text romanesc pentru procesare NLP reproductibila."""
    text = unicodedata.normalize("NFC", text)
    text = text.translate(QUOTE_MAP)
    text = ZERO_WIDTH_RE.sub("", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(SPACE_RE.sub(" ", line).strip() for line in text.split("\n"))
    text = MULTI_NEWLINE_RE.sub("\n\n", text).strip()
    return text.lower() if lowercase else text


def normalize_rows(
    rows: list[dict[str, object]], text_key: str = "text"
) -> list[dict[str, object]]:
    normalized: list[dict[str, object]] = []
    for row in rows:
        copy = dict(row)
        value = copy.get(text_key)
        if isinstance(value, str):
            copy[text_key] = normalize_text(value)
        normalized.append(copy)
    return normalized


from __future__ import annotations

import re

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE_RE = re.compile(
    r"(?<!\d)(?:\+?40|0)\s?(?:7\d{2}|2\d{2}|3\d{2})[\s.-]?\d{3}[\s.-]?\d{3}(?!\d)"
)
CNP_RE = re.compile(r"(?<!\d)[1-9]\d{12}(?!\d)")
IBAN_RE = re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9 ]{11,30}\b")


def mask_personal_data(text: str) -> str:
    text = EMAIL_RE.sub("[EMAIL]", text)
    text = PHONE_RE.sub("[TELEFON]", text)
    text = CNP_RE.sub("[CNP]", text)
    text = IBAN_RE.sub("[IBAN]", text)
    return text


def contains_personal_data(text: str) -> bool:
    return any(regex.search(text) for regex in (EMAIL_RE, PHONE_RE, CNP_RE, IBAN_RE))


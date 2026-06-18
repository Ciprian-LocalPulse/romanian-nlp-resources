from __future__ import annotations

import csv
from pathlib import Path


def csv_manifest_to_records(path: str | Path) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            duration = row.get("duration_sec") or None
            records.append(
                {
                    "id": row["id"],
                    "audio_path": row["audio_path"],
                    "transcript": row["transcript"],
                    "duration_sec": float(duration) if duration is not None else None,
                    "speaker_id": row.get("speaker_id") or None,
                    "split": row.get("split") or "train",
                    "license": row.get("license") or None,
                }
            )
    return records


def edit_distance(left: list[str] | str, right: list[str] | str) -> int:
    rows = len(left) + 1
    cols = len(right) + 1
    dp = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        dp[i][0] = i
    for j in range(cols):
        dp[0][j] = j
    for i in range(1, rows):
        for j in range(1, cols):
            cost = 0 if left[i - 1] == right[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    return dp[-1][-1]


def wer(reference: str, hypothesis: str) -> float:
    ref_words = reference.split()
    if not ref_words:
        return 0.0 if not hypothesis.split() else 1.0
    return edit_distance(ref_words, hypothesis.split()) / len(ref_words)


def cer(reference: str, hypothesis: str) -> float:
    if not reference:
        return 0.0 if not hypothesis else 1.0
    return edit_distance(reference, hypothesis) / len(reference)


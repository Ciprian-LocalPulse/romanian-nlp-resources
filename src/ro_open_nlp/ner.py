from __future__ import annotations

from pathlib import Path


def _tag_from_columns(columns: list[str]) -> str:
    if len(columns) == 2:
        return columns[1]
    if len(columns) >= 10:
        misc = columns[9]
        for item in misc.split("|"):
            if item.startswith(("Ner=", "NER=", "Entity=")):
                return item.split("=", 1)[1]
        return "O"
    return columns[-1] if columns else "O"


def _token_from_columns(columns: list[str]) -> str:
    if len(columns) >= 2 and columns[0].isdigit():
        return columns[1]
    return columns[0]


def bio_entities(tokens: list[str], tags: list[str]) -> list[dict[str, object]]:
    entities: list[dict[str, object]] = []
    start: int | None = None
    label: str | None = None

    def close(end: int) -> None:
        nonlocal start, label
        if start is not None and label is not None:
            entities.append(
                {
                    "start": start,
                    "end": end,
                    "label": label,
                    "text": " ".join(tokens[start:end]),
                }
            )
        start = None
        label = None

    for index, tag in enumerate(tags):
        if tag == "O" or not tag:
            close(index)
            continue
        prefix, _, current_label = tag.partition("-")
        if prefix == "B" or current_label != label:
            close(index)
            start = index
            label = current_label or tag
        elif prefix != "I":
            close(index)
    close(len(tags))
    return entities


def conllu_to_records(path: str | Path) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    tokens: list[str] = []
    tags: list[str] = []
    sent_id = "sent-1"
    sentence_index = 1

    def flush() -> None:
        nonlocal tokens, tags, sent_id, sentence_index
        if not tokens:
            return
        records.append(
            {
                "id": sent_id,
                "text": " ".join(tokens),
                "tokens": tokens,
                "tags": tags,
                "entities": bio_entities(tokens, tags),
            }
        )
        sentence_index += 1
        sent_id = f"sent-{sentence_index}"
        tokens = []
        tags = []

    for raw_line in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            flush()
            continue
        if line.startswith("#"):
            if line.startswith("# sent_id"):
                sent_id = line.split("=", 1)[1].strip()
            continue
        columns = line.split("\t") if "\t" in line else line.split()
        if not columns or "-" in columns[0] or "." in columns[0]:
            continue
        tokens.append(_token_from_columns(columns))
        tags.append(_tag_from_columns(columns))
    flush()
    return records


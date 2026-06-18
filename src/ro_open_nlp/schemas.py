from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, field_validator


class Entity(BaseModel):
    start: int = Field(ge=0)
    end: int = Field(gt=0)
    label: str
    text: str

    @field_validator("end")
    @classmethod
    def end_after_start(cls, value: int, info):
        start = info.data.get("start")
        if start is not None and value <= start:
            raise ValueError("end trebuie sa fie mai mare decat start")
        return value


class NERRecord(BaseModel):
    id: str
    text: str
    tokens: list[str]
    tags: list[str]
    entities: list[Entity] = Field(default_factory=list)

    @field_validator("tags")
    @classmethod
    def same_length(cls, value: list[str], info):
        tokens = info.data.get("tokens")
        if tokens is not None and len(value) != len(tokens):
            raise ValueError("tokens si tags trebuie sa aiba aceeasi lungime")
        return value


class DisinformationRecord(BaseModel):
    id: str
    text: str
    label: Literal["factual", "misleading", "false", "satire", "opinion", "unverified"]
    source: str | None = None
    evidence: list[str] = Field(default_factory=list)
    annotator_notes: str | None = None
    lang: Literal["ro"] = "ro"

    @field_validator("text")
    @classmethod
    def text_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("textul nu poate fi gol")
        return value


class SpeechRecord(BaseModel):
    id: str
    audio_path: str
    transcript: str
    duration_sec: float | None = Field(default=None, ge=0)
    speaker_id: str | None = None
    split: Literal["train", "validation", "test"] = "train"
    license: str | None = None


SCHEMAS = {
    "disinformation": DisinformationRecord,
    "ner": NERRecord,
    "speech": SpeechRecord,
}


def validate_rows(rows: list[dict], schema_name: str) -> list[BaseModel]:
    if schema_name not in SCHEMAS:
        known = ", ".join(sorted(SCHEMAS))
        raise ValueError(f"Schema necunoscuta: {schema_name}. Scheme disponibile: {known}")
    model = SCHEMAS[schema_name]
    return [model.model_validate(row) for row in rows]


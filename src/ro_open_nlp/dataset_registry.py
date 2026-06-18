from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class DatasetEntry:
    name: str
    task: str
    language: str
    license: str
    source_url: str
    status: str
    notes: str = ""


def load_registry(path: str | Path = "configs/dataset_registry.yaml") -> list[DatasetEntry]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return [DatasetEntry(**item) for item in data["datasets"]]


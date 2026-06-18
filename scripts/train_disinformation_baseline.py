from __future__ import annotations

import argparse
import json
from pathlib import Path

from ro_open_nlp.io import read_jsonl


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", required=True)
    parser.add_argument("--output", default="models/disinformation_baseline_report.json")
    args = parser.parse_args()

    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import cross_val_score
        from sklearn.pipeline import Pipeline
    except ImportError as exc:
        raise SystemExit('Instaleaza dependintele ML: pip install -e ".[ml]"') from exc

    rows = read_jsonl(args.train)
    texts = [row["text"] for row in rows]
    labels = [row["label"] for row in rows]
    if len(set(labels)) < 2:
        raise SystemExit("Ai nevoie de cel putin doua clase pentru antrenare.")

    pipeline = Pipeline(
        [
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
            ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
        ]
    )
    cv = min(5, len(rows))
    scores = cross_val_score(pipeline, texts, labels, cv=cv, scoring="f1_macro")
    report = {
        "rows": len(rows),
        "classes": sorted(set(labels)),
        "cv": cv,
        "macro_f1_mean": float(scores.mean()),
        "macro_f1_std": float(scores.std()),
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()


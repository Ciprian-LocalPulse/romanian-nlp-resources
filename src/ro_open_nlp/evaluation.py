from __future__ import annotations

from collections import Counter


def precision_recall_f1(tp: int, fp: int, fn: int) -> dict[str, float]:
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"precision": precision, "recall": recall, "f1": f1}


def entity_f1(gold: list[dict], predicted: list[dict]) -> dict[str, float]:
    gold_set = {(e["start"], e["end"], e["label"]) for e in gold}
    pred_set = {(e["start"], e["end"], e["label"]) for e in predicted}
    tp = len(gold_set & pred_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    return precision_recall_f1(tp, fp, fn)


def classification_report(gold: list[str], predicted: list[str]) -> dict[str, dict[str, float]]:
    labels = sorted(set(gold) | set(predicted))
    report: dict[str, dict[str, float]] = {}
    for label in labels:
        tp = sum(g == label and p == label for g, p in zip(gold, predicted, strict=False))
        fp = sum(g != label and p == label for g, p in zip(gold, predicted, strict=False))
        fn = sum(g == label and p != label for g, p in zip(gold, predicted, strict=False))
        report[label] = precision_recall_f1(tp, fp, fn)
    counts = Counter(gold)
    total = sum(counts.values()) or 1
    report["weighted_avg"] = {
        metric: sum(report[label][metric] * counts[label] for label in labels) / total
        for metric in ("precision", "recall", "f1")
    }
    return report


from ro_open_nlp.evaluation import classification_report, entity_f1


def test_entity_f1_exact():
    gold = [{"start": 0, "end": 1, "label": "PER"}]
    pred = [{"start": 0, "end": 1, "label": "PER"}]
    assert entity_f1(gold, pred)["f1"] == 1.0


def test_classification_report():
    report = classification_report(["a", "b"], ["a", "a"])
    assert "weighted_avg" in report


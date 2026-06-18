from ro_open_nlp.ner import bio_entities, conllu_to_records


def test_bio_entities():
    tokens = ["Ana", "merge", "la", "Cluj"]
    tags = ["B-PER", "O", "O", "B-LOC"]
    entities = bio_entities(tokens, tags)
    assert entities == [
        {"start": 0, "end": 1, "label": "PER", "text": "Ana"},
        {"start": 3, "end": 4, "label": "LOC", "text": "Cluj"},
    ]


def test_conllu_sample():
    records = conllu_to_records("data/samples/ner/sample.conllu")
    assert len(records) == 2
    assert records[0]["entities"][0]["label"] == "PER"


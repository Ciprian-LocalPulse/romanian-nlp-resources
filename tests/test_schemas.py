from ro_open_nlp.io import read_jsonl
from ro_open_nlp.schemas import validate_rows


def test_disinformation_sample_validates():
    rows = read_jsonl("data/samples/disinformation/sample.jsonl")
    assert len(validate_rows(rows, "disinformation")) == 3


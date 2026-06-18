from ro_open_nlp.privacy import mask_personal_data
from ro_open_nlp.quality import text_quality_score


def test_mask_personal_data():
    text = "Scrie la test@example.com sau suna la 0712 345 678."
    masked = mask_personal_data(text)
    assert "[EMAIL]" in masked
    assert "[TELEFON]" in masked


def test_quality_penalizes_personal_data():
    score = text_quality_score("Contact: test@example.com pentru detalii despre proiect.")
    assert score["contains_personal_data"] is True
    assert score["score"] < 1.0


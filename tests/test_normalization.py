from ro_open_nlp.normalization import normalize_text


def test_normalize_text_spaces_and_quotes():
    text = "  „Ana\u00a0 merge”   \n\n\n"
    assert normalize_text(text) == '"Ana merge"'


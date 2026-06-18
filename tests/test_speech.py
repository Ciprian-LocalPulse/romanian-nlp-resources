from ro_open_nlp.speech import cer, wer


def test_wer_and_cer():
    assert wer("ana merge acasa", "ana merge") == 1 / 3
    assert cer("abc", "adc") == 1 / 3


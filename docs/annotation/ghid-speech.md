# Ghid pentru speech-to-text romanesc

## Manifest

Campuri minime:

- `id`
- `audio_path`
- `transcript`
- `duration_sec`
- `speaker_id`
- `split`
- `license`

## Transcripturi

- Pastreaza diacriticele.
- Marcheaza ezitarile doar daca proiectul cere asta explicit.
- Nu corecta gramatical vorbitorul daca obiectivul este ASR realist.
- Normalizeaza cifrele conform protocolului de evaluare.

## Evaluare

- WER: rata erorilor la nivel de cuvant.
- CER: rata erorilor la nivel de caracter.
- Raporteaza separat pe accent, gen auto-raportat, calitate audio si domeniu, daca datele permit si consimtamantul exista.


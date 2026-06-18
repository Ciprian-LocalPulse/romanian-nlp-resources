# Baseline NER romanesc

## Scop

Model de referinta pentru NER in romana, bazat pe un encoder transformer romanesc sau multilingv.

## Date

Datele trebuie furnizate de utilizator in format JSONL conform `docs/schemas/jsonl.md`.

## Metrice recomandate

- precision strict la nivel de entitate;
- recall strict la nivel de entitate;
- F1 strict la nivel de entitate;
- analiza erorilor pe clase.

## Limitari

Baseline-ul poate sub-performa pe texte istorice, dialectale, informale sau domenii specializate.


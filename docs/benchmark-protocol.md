# Protocol de benchmark

## Splituri

Recomandare implicita:

- train: 80%
- validation: 10%
- test: 10%

Pentru corpusuri mici, foloseste cross-validation si publica seedurile.

## Metrice

| Sarcina | Metrice |
|---|---|
| NER | entity-level precision, recall, F1 strict |
| Clasificare | macro-F1, accuracy, calibration |
| Speech-to-text | WER, CER |
| Retrieval/QA | exact match, F1, recall@k |

## Raportare

Publica:

- versiunea datelor;
- hashurile fisierelor;
- seedurile;
- configuratia modelului;
- hardware-ul;
- durata antrenarii;
- limitari si erori frecvente.


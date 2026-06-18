# Publicare pe Hugging Face

## Recomandari

- Publica doar date cu licenta compatibila.
- Include `README.md` de dataset cu card complet.
- Include script de incarcare sau fisiere JSONL/CSV standard.
- Adauga taguri: `romanian`, `nlp`, `ner`, `speech-recognition`, `disinformation`.
- Mentioneaza clar daca datele sunt sintetice, derivate sau colectate manual.

## Structura minima

```text
dataset/
├── README.md
├── train.jsonl
├── validation.jsonl
└── test.jsonl
```


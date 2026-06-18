# Contributii

Multumim ca vrei sa ajuti limba romana sa aiba resurse NLP mai bune.

## Tipuri de contributii

- Dataset nou sau extindere pentru un dataset existent.
- Script de import, curatare, validare sau conversie.
- Baseline de model sau protocol de evaluare.
- Documentatie, traduceri, exemple, issue-uri de calitate.

## Cerinte pentru date

1. Include licenta si sursa.
2. Include card de dataset.
3. Include mostre mici in `data/samples/`.
4. Ruleaza validarile.
5. Documenteaza riscurile: bias, confidentialitate, acoperire dialectala, erori de adnotare.

## Stil cod

```bash
ruff check .
pytest
```

Foloseste functii mici, teste clare si configuratii declarative in `configs/`.


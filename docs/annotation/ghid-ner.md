# Ghid de adnotare NER pentru romana

## Etichete

- `PER`: persoane reale sau fictive.
- `ORG`: organizatii, companii, universitati, ONG-uri, institutii.
- `LOC`: locatii geografice, orase, rauri, munti.
- `GPE`: tari, judete, unitati politico-administrative.
- `TIME`: expresii temporale vagi sau recurente.
- `DATE`: date calendaristice.
- `EVENT`: evenimente numite.
- `PRODUCT`: produse, servicii sau tehnologii numite.
- `LAW`: acte normative.
- `WORK`: lucrari, carti, publicatii, opere.

## Format

Folosim BIO:

- `B-LABEL`: inceput de entitate.
- `I-LABEL`: continuare de entitate.
- `O`: in afara entitatii.

## Exemple

```text
Ana B-PER
lucreaza O
la O
Universitatea B-ORG
din I-ORG
Bucuresti I-ORG
. O
```

## Reguli dificile

- "Guvernul Romaniei" este `ORG`.
- "Romania" ca stat este `GPE`; ca locatie geografica poate fi `LOC`, in functie de schema proiectului.
- Titlurile precum "doctor", "profesor", "presedinte" nu intra in `PER` decat daca fac parte din numele oficial.
- Pentru organizatii cu prepozitii interne, include prepozitia daca face parte natural din nume: "Universitatea din Bucuresti".


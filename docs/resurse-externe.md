# Resurse externe pentru NLP romanesc

Aceasta lista este un punct de pornire. Inainte de folosire, verifica mereu licenta curenta, termenii platformei si modul permis de redistribuire.

## NER si analiza text

| Resursa | Utilitate | Observatii |
|---|---|---|
| RONEC | NER romanesc | Corpus public pentru entitati numite, disponibil in formate BRAT si CoNLL-U Plus. |
| HistNERo | NER istoric | Ziare istorice romanesti, util pentru robustete pe texte vechi. |
| Universal Dependencies Romanian RRT | morfologie, sintaxa | Treebank romanesc pentru parsare si taguire. |
| Romanian BERT | reprezentari contextuale | Model romanesc dedicat, util pentru baseline-uri. |
| RoBERTweet | social media | Model/corpus pentru tweet-uri romanesti, necesita atentie la termenii platformei. |

## Speech

| Resursa | Utilitate | Observatii |
|---|---|---|
| Mozilla Common Voice | speech-to-text, TTS, evaluare | Date vocale crowdsource, licenta CC0 pentru seturile publicate; verifica versiunea. |

## Dezinformare, clickbait si satira

| Resursa | Utilitate | Observatii |
|---|---|---|
| RoCliCo | clickbait romanesc | Corpus pentru titluri/articole clickbait. |
| MuSaRoNews | satira multimodala | Corpus romanesc pentru satira in stiri. |
| SaRoHead | satira in headline-uri | Util pentru detectarea titlurilor satirice. |
| SeLeRoSa | satira la nivel de propozitie | Granularitate utila pentru analiza fina. |

## Reguli de includere in RoOpenNLP

1. Nu copia datele in repository daca licenta nu permite redistribuirea.
2. Pastreaza doar mostre sintetice sau permise explicit.
3. Scrie un script de import care descarca datele de la sursa oficiala.
4. Completeaza cardul de dataset.
5. Mentioneaza citarea academica recomandata de autorii resursei.


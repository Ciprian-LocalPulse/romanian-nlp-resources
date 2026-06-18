.PHONY: test lint format validate-samples

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

validate-samples:
	ro-open-nlp validate data/samples/disinformation/sample.jsonl --schema disinformation
	ro-open-nlp conllu-to-jsonl data/samples/ner/sample.conllu --output data/interim/ner.jsonl
	ro-open-nlp speech-manifest data/samples/speech/manifest.csv --output data/interim/speech_manifest.jsonl


from __future__ import annotations

import argparse
from pathlib import Path

from pydantic import ValidationError

from ro_open_nlp.io import read_jsonl, read_text, write_jsonl, write_text
from ro_open_nlp.ner import conllu_to_records
from ro_open_nlp.normalization import normalize_text
from ro_open_nlp.schemas import validate_rows
from ro_open_nlp.speech import csv_manifest_to_records


def normalize_text_command(args: argparse.Namespace) -> None:
    write_text(args.output, normalize_text(read_text(args.input_path), lowercase=args.lowercase))
    print(f"Text normalizat: {args.output}")


def conllu_to_jsonl_command(args: argparse.Namespace) -> None:
    input_path = args.input_path
    output = args.output
    rows = conllu_to_records(input_path)
    validate_rows(rows, "ner")
    write_jsonl(output, rows)
    print(f"Convertit {len(rows)} propozitii NER: {output}")


def speech_manifest_command(args: argparse.Namespace) -> None:
    input_path = args.input_path
    output = args.output
    rows = csv_manifest_to_records(input_path)
    validate_rows(rows, "speech")
    write_jsonl(output, rows)
    print(f"Manifest speech valid: {output}")


def validate_command(args: argparse.Namespace) -> None:
    rows = read_jsonl(args.input_path)
    try:
        validated = validate_rows(rows, args.schema)
    except ValidationError as exc:
        raise SystemExit(f"Validare esuata:\n{exc}") from exc
    print(f"Validare OK | schema={args.schema} | randuri={len(validated)}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ro-open-nlp", description="CLI pentru RoOpenNLP.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    normalize = subparsers.add_parser("normalize-text")
    normalize.add_argument("input_path", type=Path)
    normalize.add_argument("--output", "-o", type=Path, required=True)
    normalize.add_argument("--lowercase", action="store_true")
    normalize.set_defaults(func=normalize_text_command)

    conllu = subparsers.add_parser("conllu-to-jsonl")
    conllu.add_argument("input_path", type=Path)
    conllu.add_argument("--output", "-o", type=Path, required=True)
    conllu.set_defaults(func=conllu_to_jsonl_command)

    speech = subparsers.add_parser("speech-manifest")
    speech.add_argument("input_path", type=Path)
    speech.add_argument("--output", "-o", type=Path, required=True)
    speech.set_defaults(func=speech_manifest_command)

    validate = subparsers.add_parser("validate")
    validate.add_argument("input_path", type=Path)
    validate.add_argument("--schema", required=True, choices=["disinformation", "ner", "speech"])
    validate.set_defaults(func=validate_command)
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()

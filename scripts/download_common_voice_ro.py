"""Ghid executabil pentru descarcarea Common Voice romana prin Hugging Face.

Scriptul evita descarcarea automata fara consimtamant. Completeaza parametrii
si ruleaza local dupa ce ai verificat licenta si termenii datasetului.
"""

from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="latest", help="Versiunea Common Voice dorita.")
    parser.add_argument("--split", default="train", help="Split: train/validation/test.")
    args = parser.parse_args()
    print(
        "Pentru descarcare, foloseste pachetul datasets si datasetul Common Voice. "
        f"Versiune ceruta: {args.version}, split: {args.split}. "
        "Verifica manual licenta CC0 si termenii curenti inainte de redistribuire."
    )


if __name__ == "__main__":
    main()


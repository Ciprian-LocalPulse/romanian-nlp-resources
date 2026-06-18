from __future__ import annotations

import argparse
from pathlib import Path

TEMPLATE = """# {name}

## Rezumat

## Sursa

## Licenta

## Schema

## Procesare

## Splituri

## Riscuri si limitari

## Citare
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    output = Path(args.output or f"docs/datasets/{args.name.lower().replace(' ', '-')}.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEMPLATE.format(name=args.name), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()


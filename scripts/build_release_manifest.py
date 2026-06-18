from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", help="Directorul care va fi inclus in manifest.")
    parser.add_argument("--output", default="outputs/release_manifest.json")
    args = parser.parse_args()

    root = Path(args.root)
    files = []
    for path in sorted(root.rglob("*")):
        if path.is_file():
            files.append(
                {
                    "path": str(path.as_posix()),
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"root": str(root), "files": files}, indent=2), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()


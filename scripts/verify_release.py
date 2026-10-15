"""Verify archived evidence integrity without third-party dependencies."""

import hashlib
import json
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    release = json.loads((ROOT / "DATA_MANIFEST.json").read_text(encoding="utf-8"))
    source = json.loads((ROOT / "source_evidence_manifest.json").read_text(encoding="utf-8"))
    files = release["files"]
    if not files:
        raise SystemExit("Empty data manifest")
    archive = ROOT / "evidence.zip"
    expected_archive = (ROOT / "ARCHIVE_SHA256.txt").read_text(encoding="ascii").split()[0]
    if digest(archive) != expected_archive:
        raise SystemExit("Evidence ZIP checksum mismatch")
    with ZipFile(archive) as zf:
        actual = set(zf.namelist())
        if actual != set(files):
            raise SystemExit("Unexpected or unmanifested evidence file")
        for rel, expected in files.items():
            if hashlib.sha256(zf.read(rel)).hexdigest() != expected:
                raise SystemExit(f"Missing or changed release file: {rel}")
        for rel, expected in source["evidence_sha256"].items():
            if hashlib.sha256(zf.read("evidence/" + rel)).hexdigest() != expected:
                raise SystemExit(f"Missing or changed core evidence: {rel}")
    print(f"Verified {len(files)} release files and {len(source['evidence_sha256'])} core hashes")


if __name__ == "__main__":
    main()

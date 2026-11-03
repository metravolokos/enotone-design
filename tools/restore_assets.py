#!/usr/bin/env python3
"""Restore the exact approved enoTone graphics from Git-tracked bundle parts.

Run from any location:
    python tools/restore_assets.py

No third-party Python dependencies are required.
"""
from __future__ import annotations

import hashlib
import io
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = ROOT / "assets" / "packages"
EXPECTED_ZIP_SHA256 = "d1ff1752b73d468e8b063e715b464d19f76d69e84d180e65dd0c9230f21393c1"
EXPECTED_SOURCE_SHA256 = {
    "assets/references/bandit-10-approved.png": "c1a0910f546a9802c68d2708216dd5523f9d2214f9a432c0373caceaa48fc923",
    "assets/references/ui-palette-approved.jpg": "b479b3f0c4fb2fa057c44c3e84e09e09b591f5e64bbe7e58ebb4eea992df1616",
    "assets/icons/originals/four-icon-board.png": "28a74989c646367824c6830aa3d542c6f8bb2d1048a89cce94e951dcff805db6",
}

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main() -> None:
    parts = sorted(PACKAGES.glob("approved-assets.zip.part*"))
    if len(parts) != 5:
        raise SystemExit(f"Ожидалось 5 частей архива, найдено {len(parts)}: {PACKAGES}")
    binary = b"".join(p.read_bytes() for p in parts)
    digest = sha256(binary)
    if digest != EXPECTED_ZIP_SHA256:
        raise SystemExit(f"Ошибка SHA-256 архива: {digest}")
    count = 0
    with zipfile.ZipFile(io.BytesIO(binary)) as archive:
        damaged = archive.testzip()
        if damaged:
            raise SystemExit(f"CRC-ошибка архива: {damaged}")
        for member in archive.infolist():
            target = (ROOT / member.filename).resolve()
            if not target.is_relative_to(ROOT.resolve()) or member.is_dir():
                raise SystemExit(f"Некорректная запись в архиве: {member.filename}")
            data = archive.read(member)
            expected = EXPECTED_SOURCE_SHA256.get(member.filename)
            if expected and sha256(data) != expected:
                raise SystemExit(f"Не совпадает SHA-256: {member.filename}")
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists() or target.read_bytes() != data:
                target.write_bytes(data)
            count += 1
    print(f"Готово: восстановлено и проверено {count} графических файлов.")
    print("Изображения и иконки не перерисованы и не пересжаты.")

if __name__ == "__main__":
    main()

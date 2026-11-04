#!/usr/bin/env python3
"""Pure-stdlib deterministic verification of all current design assets and Android XML.
Run from project root: python3 tools/verify_enotone_assets.py
"""
import argparse, hashlib, json, xml.etree.ElementTree as ET
from pathlib import Path
root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--smoke-only', action='store_true', help='Verify supplied APK resources; full artwork import remains pending')
args=parser.parse_args()
file=root/('android-icon-smoke/RESOURCES.sha256' if args.smoke_only else 'assets/current/CHECKSUMS.sha256')
passed=0
for line in file.read_text(encoding='utf8').splitlines():
    if not line or line.startswith('#'):continue
    sha, relative=line.split('  ',1)
    assert len(sha)==64
    f=root/relative
    assert f.is_file(),f'Missing: {relative}'
    digest=hashlib.sha256(f.read_bytes()).hexdigest()
    assert digest==sha, f'Checksum mismatch: {relative} expected {sha} actual {digest}'
    passed+=1
android=root/'android-icon-smoke/app/src/main'
ET.parse(android/'AndroidManifest.xml')
aliases=ET.parse(android/'AndroidManifest.xml').getroot().find('application').findall('activity-alias')
assert len(aliases)==6, f'Expected six testing aliases, got {len(aliases)}'
for file in (android/'res/mipmap-anydpi-v26').glob('*.xml'):ET.parse(file)
for file in (android/'res/values').glob('*.xml'):ET.parse(file)
if not args.smoke_only:
    assert (root/'assets/current/app-icon/v1.0').exists()
    assert (root/'assets/current/ui-baseline/v1.0').exists()
    assert (root/'assets/current/mascot/v20261104').exists()
java = (android/'java/app/enotone/icontest/MainActivity.java').read_text(encoding='utf8')
assert r'\n2.' in java, 'Expected Java string-escaped newlines in UI checklist'
print(f'OK: {passed} SHA256 checks, 6 launcher aliases, XML parsed')
if args.smoke_only:
    print('SMOKE ONLY: full 37-file artwork verification pending seven remaining archives')

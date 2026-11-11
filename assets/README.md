# Archived source graphics

These legacy graphics are preserved byte-for-byte inside `assets/packages/approved-assets.zip.part01`–`part05`.
Run `python tools/restore_assets.py` at the repository root after cloning to restore the historical 12 PNG/JPG files to `assets/`.

The ten-scene Bandit collage, earlier icon board, palette, and their PNG exports are historical references only. They were superseded by the user-approved 13-image Bandit set and later approved icon masters. Do not use these legacy variants in new designs; preserve them for provenance and history.

The 13-image Bandit set, approved icon originals, palette board, UI screenshots, and wordmark exports are imported under `assets/current/` from the stage 2 Git handoff. Their hashes are recorded in `assets/current/CHECKSUMS.sha256`; `python3 tools/verify_enotone_assets.py` verifies all 37 declared files. The legacy archive above remains historical and is not an active design source. See `docs/ASSET_POLICY.md` and `docs/DESIGN_DECISIONS.md` for the active source hierarchy.

**The `.part` files are binary data, not images for direct viewing. Do not edit or recompress them.**

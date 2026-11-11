# First Codex Cloud task — enoTone design asset migration and Android icon smoke test

Branch: `feature/enotone-icon-smoke-20261104` (do not commit directly to `main`).
Scope: `metravolokos/enotone-design` only. Review AGENTS.md and all current docs.

1. Import files from this handoff ZIP, preserving exact bytes in `assets/current/`.
   No regeneration and no editing of approved originals.
   Verify each SHA256 with `python3 tools/verify_enotone_assets.py`.
2. Mark old `assets/packages/approved-assets.zip.part*` and earlier
   mascot/icon sources as historical; prevent automatic restoration into `assets/current`.
   Do not purge git history. Prefer `assets/archive/` or documentation instead of risky deletions.
3. Build separate `android-icon-smoke` project (no production player, no network
   credentials, no Google Play Services). JDK21, SDK35, Gradle8.13, AGP8.11.1.
   `source /workspace/enotone-tools/env.sh` then run `gradle :app:assembleDebug`.
4. Add/validate GitHub Actions build with artifact upload. Run CI and show
   concrete run URL plus artifact name; debug signing only.
5. **Stop at Draft PR**. No merge without user acceptance of installed APK on Huawei Nova 15 Pro.
   Request manual verification of six icons and report mask/pointer/ears/fringing.
6. Never do ADB checks or connect a phone unless user starts a separate ADB task.
   No background agent/coordinator or release credentials. Preserve existing wordmark.

Acceptance: SHA256 for every original; Android APK verified; CI artifact available;
Draft PR; no changes to other repos; no false claims about device testing.
If build blocked, provide logs, exact blocker and local results; do not fake success.

# Instructions for AI agents — enoTone Design

Language: discuss decisions with the user in Russian. Keep technical identifiers, assets and filenames unchanged.

Start with `docs/DESIGN_DECISIONS.md` — it lists everything that is in force now. Anything not described there or in the documents it links to is not approved.

1. **Scope.** Design-only repository. Never modify or dispatch changes to the AllMusic repositories or playback engines unless the user explicitly changes scope. No credentials or private WebDAV data here.
2. **Names.** Product **enoTone** (always capital `T`), mascot **Бандит**. Do not rename.
3. **Generated assets — never edit by hand.** Change the script and rebuild:
   - app icon v2.0 → `tools/build_app_icon.py` → `assets/icons/v2.0/` ([APP_ICON_V2](docs/APP_ICON_V2.md)); one icon on Graphite `#1B1A19`, no light variant; monochrome deferred by the user;
   - UI Icons v1 → `tools/build_ui_icons.py` → `assets/ui-icons/v1/` ([UI_ICONS_V1](docs/UI_ICONS_V1.md)); category and playback icons come ONLY from this set, Material Symbols Rounded only for missing utility icons;
   - Wordmark v2.0 → `tools/build_wordmark.py` → `assets/wordmark/v2/` ([WORDMARK_V2](docs/WORDMARK_V2.md)); never draw it by hand or set it in a font; shown in the app only in Settings and About;
   - cleaned Bandit → `tools/clean_bandit.py` → `assets/bandit/clean/`.
4. **Bandit.** The only character is the cartoon Bandit in `assets/bandit/originals/` (keep byte-for-byte) and `assets/bandit/masters/`. Never redraw, regenerate or approximate him; only scale, crop, mask. Screen assignments and rules — [BANDIT_SET_V1](docs/BANDIT_SET_V1.md). The pointing pose belongs to the app icon only.
5. **Style.** «Глянцевый енот», themes «Графит» and «Фарфор»; palette locked to `tokens/colors.json` v1.3. Fonts: Unbounded for headings, Onest elsewhere. New colour or state tokens need the owner's approval.
6. **Android screens.** Approved reference: `assets/ui-screens/android-v2/` and [UI_ANDROID_V2](docs/UI_ANDROID_V2.md); reference device Huawei Nova 15 Pro, 377 × 816 dp, corner radius ≈ 56 dp. Change a screen on the canvas first, then re-export PNG and update `SHA256SUMS`. The bottom-bar label for album artists is **«Авторы»**, screen title **«Авторы альбомов»**.
7. **Android integration.** Merge order and steps D0–D6 — [ANDROID_INTEGRATION_PLAN](docs/ANDROID_INTEGRATION_PLAN.md). This repository is the only source of design assets; the app copies them from `main` unchanged.
8. **Desktop.** Working direction is the Desktop part of [UI_BASELINE_V1](docs/UI_BASELINE_V1.md); postponed. Keep Desktop and Android layouts separate while sharing tokens.
9. **Recording changes.** Every approved change: a dated entry in `docs/CHANGELOG.md` and an update of `docs/DESIGN_DECISIONS.md`. Verify originals with SHA-256.
10. **Removed history.** Superseded decisions (old 10-scene Bandit collage and ZIP parts, app icon v1.0 and platform packs, Android adaptive color v2, Wordmark Master v1.0, Bandit SVG candidates, MVP-reset and minimal-direction briefs) were deleted on 2026-11-13. They exist only in Git history up to commit `dd0c101`; never restore them into current work.

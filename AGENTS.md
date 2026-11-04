# Instructions for AI agents — enoTone Design

Language: discuss decisions with the user in Russian. Keep technical identifiers, assets and filenames unchanged.

1. This repository is a **design-only** workspace. Never modify or dispatch changes to the existing AllMusic repositories or playback engines unless user explicitly changes scope.
2. Product name: **enoTone**, always spelled with capital `T`. Mascot: **Бандит**. Do not rename.
3. IMPORTANT SUPERSESSION: the user replaced the old 10-scene mascot with **13 newly supplied Bandit PNGs** on 2026-11-04. The Git-tracked `assets/references/bandit-10-approved.png` and its ZIP backup are historical and MUST NOT be used in new UI. New PNGs are not yet uploaded to GitHub; do not approximate, regenerate or silently restore the older character. Keep current Bandit unchanged once imported.
4. The four app icon artworks are approved in `assets/icons/originals/four-icon-board.png`; do not redraw. Separate square/round and light/dark raster exports are derivative mockup assets.
5. Approved current style is **«Глянцевый енот»** with themes **«Графит»** and **«Фарфор»**. Palette is locked to `tokens/colors.json` (version 1.3), based on the user-supplied board `Основа палитра и стиль@2x.png`; the former `assets/references/ui-palette-approved.jpg` is historical, not normative. Fonts: **Unbounded** for headings, **Onest** elsewhere. Large 16–28 px radii, circular Play, selective glaze effects. Additional semantic/UI state tokens require review.
6. Altering original pixels, introducing SVG icons based on approximation, or claiming vector/adaptive resources exist when they don't is prohibited.
7. The 10 user-provided UI reference screenshots form **UI Baseline v1.0** (see `docs/UI_BASELINE_V1.md`): working visual/layout direction for 5 Desktop + 5 Android screens, both themes. They are NOT an implemented app, pixel-perfect approval or a license to change audio engines. Specific sizes, breakpoints, interactions, motion and state designs remain unapproved; mark proposals as drafts.
8. Future implementations should keep desktop and Android screen layouts separate while sharing theme tokens; no code has been approved for integration.
9. Record every approved change with a date in `docs/CHANGELOG.md` and a revision of `docs/DESIGN_DECISIONS.md`. Use SHA-256 to verify originals.
10. No credentials or private WebDAV data in this repository.
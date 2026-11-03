# Instructions for AI agents — enoTone Design

Language: discuss decisions with the user in Russian. Keep technical identifiers, assets and filenames unchanged.

1. This repository is a **design-only** workspace. Never modify or dispatch changes to the existing AllMusic repositories or playback engines unless user explicitly changes scope.
2. Product name: **enoTone**, always spelled with capital `T`. Mascot: **Бандит**. Do not rename.
3. The single approved 10-scene mascot source is `assets/references/bandit-10-approved.png`. Do not regenerate, deform, crop important body parts/props, recolor or slim the character. Preserve all ten scenes; the previous 7-image selection is superseded.
4. The four app icon artworks are approved in `assets/icons/originals/four-icon-board.png`; do not redraw. Separate square/round and light/dark raster exports are derivative mockup assets.
5. Palette is locked to `tokens/colors.json` (as specified by `assets/references/ui-palette-approved.jpg`). Additional semantic/UI state tokens require review.
6. Altering original pixels, introducing SVG icons based on approximation, or claiming vector/adaptive resources exist when they don't is prohibited.
7. New UI screen layouts, typography, navigation, motion and component choices remain **unapproved**. Mark all proposals explicitly as drafts.
8. Future implementations should keep desktop and Android screen layouts separate while sharing theme tokens; no code has been approved for integration.
9. Record every approved change with a date in `docs/CHANGELOG.md` and a revision of `docs/DESIGN_DECISIONS.md`. Use SHA-256 to verify originals.
10. No credentials or private WebDAV data in this repository.
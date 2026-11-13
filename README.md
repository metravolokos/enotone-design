# enoTone — дизайн

Дизайн-репозиторий персонального музыкального плеера **enoTone** и его маскота **Бандита**. Здесь лежат утверждённые ресурсы и решения; приложение ([enoTone-android](https://github.com/metravolokos/enoTone-android)) копирует ресурсы отсюда без изменений.

Все действующие решения кратко — [`docs/DESIGN_DECISIONS.md`](docs/DESIGN_DECISIONS.md), история — [`docs/CHANGELOG.md`](docs/CHANGELOG.md).

## Что утверждено

| Что | Документ | Файлы | Источник |
| --- | --- | --- | --- |
| Палитра «Глянцевый енот» v1.3, темы «Графит» и «Фарфор» | [DESIGN_DECISIONS §4](docs/DESIGN_DECISIONS.md) | `tokens/colors.json` | — |
| Иконка приложения v2.0 | [APP_ICON_V2](docs/APP_ICON_V2.md) | `assets/icons/v2.0/` | `tools/build_app_icon.py` |
| Текстовый логотип Wordmark v2.0 | [WORDMARK_V2](docs/WORDMARK_V2.md) | `assets/wordmark/v2/` | `tools/build_wordmark.py` |
| Значки интерфейса UI Icons v1 | [UI_ICONS_V1](docs/UI_ICONS_V1.md) | `assets/ui-icons/v1/` | `tools/build_ui_icons.py` |
| Бандит: 13 поз и назначение по экранам | [BANDIT_SET_V1](docs/BANDIT_SET_V1.md) | `assets/bandit/` | `tools/clean_bandit.py` |
| Экраны Android UI v2 (Nova 15 Pro, 377 × 816 dp) | [UI_ANDROID_V2](docs/UI_ANDROID_V2.md) | `assets/ui-screens/android-v2/` | холст в claude.ai |
| Перенос в приложение (этапы D0–D6) | [ANDROID_INTEGRATION_PLAN](docs/ANDROID_INTEGRATION_PLAN.md) | — | — |
| Desktop — рабочее направление (отложено) | [UI_BASELINE_V1](docs/UI_BASELINE_V1.md) | — | — |

Шрифты: **Unbounded** — заголовки, **Onest** — всё остальное.

## Структура

```text
assets/
  bandit/originals/     13+1 изображений Бандита от владельца — не изменять
  bandit/clean/         те же с исправленной прозрачностью
  bandit/masters/       прозрачный мастер для иконки — не изменять
  icons/v2.0/           иконка приложения и Android-ресурсы
  ui-icons/v1/          значки: SVG и Android VectorDrawable
  wordmark/v2/          логотип: SVG, PNG, Android drawable
  ui-screens/android-v2/ эталонные экраны Android (PNG, исходники холста)
docs/                   решения и описания
tokens/colors.json      палитра
tools/                  генераторы — источник истины для иконки, значков, логотипа
AGENTS.md               правила для ИИ-агентов
```

## Правила

- Файлы, которые собирают скрипты из `tools/`, руками не править: меняется скрипт, затем пересборка.
- Бандита не перерисовывать и не перегенерировать.
- Репозиторий только для дизайна; код плеера и аудиодвижков здесь не меняется.
- Отменённые решения (старый Бандит из 10 сцен, иконка v1.0, Wordmark Master v1.0, SVG-кандидаты, архивы ZIP) удалены 2026-11-13; они остаются в истории Git до коммита `dd0c101`.

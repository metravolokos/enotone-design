# Issue #3 — Android smoke, этап 1 (2026-11-04)

Источник: только `00_android_smoke_code.zip`, SHA-256 `fff4134202f182894dcb507d0a425d3d2c4207a8a3d0ecad6b861e31b1a771ec`. README пакета не заменял существующий README. `CODEX_FIRST_TASK.md` сохранён как документация передачи; актуальный объём ограничен запросом пользователя на первый этап.

## Проверки в опубликованной среде

- JDK21, SDK35, Gradle8.13, AGP8.11.1: `gradle --offline --no-daemon :app:assembleDebug` — BUILD SUCCESSFUL.
- `python3 tools/verify_enotone_assets.py --smoke-only` — 22 SHA-256 ресурсов, шесть alias и XML прошли. Все PNG и содержимое `assets/current/` совпадают с входным ZIP байт-в-байт.
- `apksigner verify --verbose` — подпись v2 прошла. `aapt dump xmltree` подтверждает шесть alias и отсутствие INTERNET permission. APK: `app.enotone.icontest`, minSdk28, targetSdk35.
- Локальный APK SHA-256: `8ebd3680b6390159e0242f700e836b326491bdc2ced15ed3ebdd5d2d13bae4c9`. CI APK имеет отдельную debug-подпись и собственный SHA, публикуемый рядом с APK.
- Локальный `lintDebug --offline`: отсутствует `com.android.tools.lint:lint-gradle:31.11.1`. Повтор без offline заблокирован DNS (`dl.google.com` и `repo.maven.apache.org`: Temporary failure in name resolution). Lint включён в CI.
- Строгая проверка без `--smoke-only` ожидаемо останавливается на отсутствующем `assets/current/app-icon/v1.0/MANIFEST.json`. Полная проверка 37 файлов НЕ завершена. Ожидаются архивы 01–07; оригиналы не восстанавливались из исторических пакетов.

## Ручная приёмка впереди

Huawei Nova 15 Pro: проверить шесть ярлыков, видимость пальца, уши, нижний край, маски и ореолы. Adaptive v2 — технический кандидат с отклонениями сегментации шерсти/теней, не художественный мастер. ADB и установка на устройство не выполнялись. Бандит не перерисовывался; wordmark не изменён. PR остаётся Draft; Issue #3 не закрывать до второго этапа и ручной приёмки.

## Результат GitHub Actions

Draft PR: https://github.com/metravolokos/enotone-design/pull/4

Run: https://github.com/metravolokos/enotone-design/actions/runs/41833315217

GitHub завершил job ошибкой до первого шага, runner_id=0, steps=[]; повторный запуск failed jobs дал тот же результат. Логи отсутствуют (BlobNotFound), artifacts=[]. Это блокер запуска CI, а не диагностированная ошибка Gradle. Сообщение annotations недоступно через подключённый API-инструмент; точная причина не подтверждена. Откройте run и проверьте аннотации GitHub, доступность Actions/runner и лимиты аккаунта.

Запасной локально собранный APK и его SHA-256 сохранены в `artifacts/icon-smoke/`; они не выдаются за CI artifact. Полная проверка всех 37 файлов и аппаратная приёмка остаются незавершёнными.

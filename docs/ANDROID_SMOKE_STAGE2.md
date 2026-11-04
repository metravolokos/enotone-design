# Issue #3 — этап 2: preflight и повторная проверка APK

**Статус:** импорт художественных оригиналов и полная проверка 37 файлов не завершены. Рабочая среда не получила семь архивов этапа 2, поэтому ниже отдельно отмечены выполненные проверки и ограничения. PR #4 остаётся Draft.

## Архивы и исходники

Последний комментарий ChatGPT в [PR #4](https://github.com/metravolokos/enotone-design/pull/4#issuecomment-6632537740) содержит имена и ожидаемые SHA-256 семи архивов `01_approved_icons.zip`–`07_ui_desktop_palette_wordmark.zip`. В `/workspace/attachments/` доступен только `00_android_smoke_code.zip`; его SHA-256 `fff4134202f182894dcb507d0a425d3d2c4207a8a3d0ecad6b861e31b1a771ec` совпадает с этапом 1. Файлов семи новых архивов в текущем checkout/вложениях нет, поэтому их SHA не сравнивались, распаковка не выполнялась.

`python3 tools/verify_enotone_assets.py` запущена без `--smoke-only` и остановилась на отсутствующем `assets/current/app-icon/v1.0/MANIFEST.json`; 37 SHA-256 не проверены. Отдельная smoke-проверка `python3 tools/verify_enotone_assets.py --smoke-only` прошла: **22 PNG SHA-256, шесть launcher alias и XML**.

Десятисценный коллаж и прежние экспорты сохраняются только для истории; использовать их в новых макетах нельзя. Актуальным источником для будущего дизайна считается утверждённый пользователем набор из 13 PNG, а для иконки — утверждённые оригиналы v1.0. До получения архивов, проверки SHA и сохранения исходных путей эти актуальные оригиналы не считаются импортированными в репозиторий.

## Android Icon Smoke Test

Чистая offline-сборка без build cache завершилась успешно:

```bash
source /workspace/enotone-tools/env.sh
export ANDROID_USER_HOME=/workspace/enotone-tools/android-user-home
gradle --offline --no-daemon --no-build-cache clean :app:assembleDebug
```

Новый локальный APK: `android-icon-smoke/app/build/outputs/apk/debug/app-debug.apk`, SHA-256 `2047b8fd9495e8182740e41c8dee381ee4521ac1077f635fb05ab428c536723d`. Подпись APK v2 проверена, пакет `app.enotone.icontest`, в manifest шесть launcher alias, разрешений нет. В частности, `INTERNET` permission отсутствует. Этот APK собран с workspace-local debug keystore и отличается по подписи от сохранённого fallback APK; fallback в Git не заменялся.

Сохранённый в PR fallback APK по-прежнему имеет SHA-256 `8ebd3680b6390159e0242f700e836b326491bdc2ced15ed3ebdd5d2d13bae4c9` и проходит проверку подписи v2, manifest и шести alias. ADB не использовался.

`lintDebug --offline` не прошёл: в кэше нет `com.android.tools.lint:lint-gradle:31.11.1`. Повтор online также не разрешил зависимость: DNS не разрешил `dl.google.com` и `repo.maven.apache.org`.

## GitHub Actions runner

[Run 41833315217, попытка 2](https://github.com/metravolokos/enotone-design/actions/runs/41833315217) завершился за три секунды до запуска шагов. И попытка 1, и попытка 2 имеют `runner_id=0`, пустые `runner_name`/`runner_group_name` и `steps=[]`; workflow просит стандартный `ubuntu-latest`. Check-run API показывает по две annotations для каждой попытки, но подключённый GitHub-инструмент не разрешает endpoint с их текстом. Получение логов вернуло `BlobNotFound`. Поэтому доказуемо только, что runner не был назначен и job не дошёл до Gradle; точная причина отказа неизвестна. Workflow не менялся.

**Чтобы завершить этап 2, нужны сами семь ZIP-файлов** с контрольными суммами из комментария выше. После их получения проверить SHA, распаковать с сохранением путей, провести строгую проверку 37 файлов, повторить APK сборку/проверки и обновить PR #4. Слияния в `main` нет.

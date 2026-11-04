# Issue #3 — этап 2: импорт исходников и проверка Android APK

**Статус:** импорт выполнен в рабочей ветке Draft PR #4. Временная ветка handoff не объединялась, ZIP в PR не добавлялись. Полная SHA-256-проверка 37 файлов и локальная чистая сборка APK прошли. Ручная проверка на Huawei остаётся открытой; ADB не использовался.

## Получение и проверка архивов

Прочитан `ARTWORK_HANDOFF_README.md` в ветке `enotone-artwork-handoff-20261104`. ZIP получены через Git fetch; временная ветка не создавалась локально и не сливалась с рабочей. SHA-256 архивов совпали с ожидаемыми значениями из README:

| ZIP | SHA-256 | Результат |
| --- | --- | --- |
| `01_enotone_artwork_A.zip` | `9844566dfd5e883554e6323ccae85aa2231aa296134ed7d204f435c0e10f22cd` | Совпадает |
| `02_enotone_artwork_B.zip` | `b14f28a94ca3e26bd9f891572a176a63da7a4bdb9d65db35a977501b92c21519` | Совпадает |

Проверены CRC ZIP, безопасные относительные пути и отсутствие повторяющихся записей. Перед импортом SHA-256 всех 35 файлов сверены с `assets/current/CHECKSUMS.sha256`. Исходная структура каталогов и байты файлов сохранены. В PR импортированы 13 изображений Бандита, 4 утверждённых оригинала иконки с манифестом и доской сравнения, исходная доска палитры, 10 UI-скриншотов, а также манифест и 4 прозрачных wordmark-экспорта. Два ранее импортированных Android Adaptive v2 файла дают итоговые 37 ресурсов. ZIP в рабочую ветку не копировались.

Полная команда `python3 tools/verify_enotone_assets.py` завершилась успешно:

```text
OK: 37 SHA256 checks, 6 launcher aliases, XML parsed
```

Таким образом, подтверждён весь набор из 37 записей в checksum-манифесте. Исторические изображения в `assets/references/` остаются архивными и не должны использоваться в новых макетах; актуальные 13 изображений находятся в `assets/current/mascot/v20261104/`.

## Android Icon Smoke Test

После импорта выполнена чистая offline-сборка без build cache:

```bash
source /workspace/enotone-tools/env.sh
export ANDROID_USER_HOME=/workspace/enotone-tools/android-user-home
cd android-icon-smoke
gradle --offline --no-daemon --no-build-cache clean :app:assembleDebug
```

Результат: `BUILD SUCCESSFUL` (33 задачи). Новый локальный APK — `android-icon-smoke/app/build/outputs/apk/debug/app-debug.apk`, SHA-256 `2047b8fd9495e8182740e41c8dee381ee4521ac1077f635fb05ab428c536723d`. `apksigner verify --verbose --print-certs` подтвердил подпись APK v2. Package: `app.enotone.icontest`; version: `0.1.0-icon-smoke`; minSdk 28, targetSdk 35. В manifest 6 launcher alias и нет разрешений, включая `INTERNET`. APK подписан локальным debug-ключом среды. Сохранённый fallback APK не заменялся; его SHA-256 остаётся `8ebd3680b6390159e0242f700e836b326491bdc2ced15ed3ebdd5d2d13bae4c9`.

`lintDebug --offline` не выполнен: в локальном кэше отсутствует `com.android.tools.lint:lint-gradle:31.11.1`; повторная online-попытка была заблокирована DNS для Maven/Google репозиториев. Это не затрагивает успешную сборку APK и проверку исходных ресурсов.

Для коммита импорта исходников `1768e1be4e6f84f321eaf9a46e1435458ea1ed22` [GitHub Actions run 41855212641](https://github.com/metravolokos/enotone-design/actions/runs/41855212641) завершился с failure до первого шага. Доступны пустой список job steps и пустой список artifacts; получение логов вернуло `BlobNotFound`. Данные не показывают причину отказа runner. Workflow не изменялся; APK Actions artifact для этого запуска не создан. Также workflow всё ещё вызывает verifier с `--smoke-only`, поэтому CI-проверка ограничена APK-ресурсами и не заменяет локальную строгую проверку 37 файлов. Полный verifier прошёл локально.

## Ограничения и замечания для приёмки

- Проверка launcher-масок на Huawei Nova 15 Pro остаётся ручной; устройство здесь не запускалось, ADB не применялся.
- Экспортный `assets/current/wordmark/v1.0/MANIFEST.json` содержит `status: candidate-for-approval`, тогда как `docs/WORDMARK_MASTER_V1.md` фиксирует отдельное окончательное утверждение мастера пользователем. Исходный handoff-манифест оставлен байт-в-байт; перед использованием экспортов как окончательных нужно независимо разрешить расхождение статусов. Утверждённый мастер не менялся.
- Свежая сборка локально подтверждена. Debug APK этого запуска остался в рабочей среде, не опубликован как GitHub Actions artifact. В репозитории сохранён более ранний fallback APK с отдельной подписью и другим SHA-256.

Все изменения передаются через существующий Draft PR #4. Слияния с `main` нет.

# enoTone — Android Icon Smoke Test

Отдельное тестовое приложение `app.enotone.icontest`, не музыкальный плеер.
Использует **4 утверждённых PNG** и **2 новых варианта adaptive v2**.
При установке намеренно создаёт **6 ярлыков**, чтобы на Huawei сравнивать
штатную маску, видимость пальца и поведение лаунчера.

## Сборка в опубликованной среде Codex Cloud

```bash
source /workspace/enotone-tools/env.sh
cd android-icon-smoke
gradle --offline :app:assembleDebug
# Если кэш AGP 8.11.1 отсутствует: gradle :app:assembleDebug
```

APK: `app/build/outputs/apk/debug/app-debug.apk`.
Установка вручную на Huawei, без ADB. Минимум Android 9 (API 28).

Предоставить подписанный штатным debug-сертификатом APK как GitHub Actions artifact;
для релизной подписи ключи не создавать и не запрашивать.

Проверки: `python3 ../tools/verify_enotone_assets.py`, затем `gradle :app:assembleDebug`.

**Известное ограничение:** foreground-сегментация v2 немного меняет границы волосков
и тени. Оригинальные PNG остаются художественным эталоном.

## Граница этого импорта

Этап 1 добавил тестовые ресурсы из `00_android_smoke_code.zip` (SHA-256 `fff4134202f182894dcb507d0a425d3d2c4207a8a3d0ecad6b861e31b1a771ec`). На этапе 2 художественные оригиналы импортированы отдельно в `assets/current/`; полный отчёт — [`docs/ANDROID_SMOKE_STAGE2.md`](../docs/ANDROID_SMOKE_STAGE2.md). `python3 tools/verify_enotone_assets.py --smoke-only` проверяет 22 PNG и шесть alias, а запуск без флага проверяет все 37 записей checksum-манифеста.

GitHub Actions должен собирать APK и выполнять lint, artifact `enotone-icon-smoke-debug-apk` содержит APK и его SHA-256 при успешном запуске. Локальная чистая offline-сборка после импорта прошла; APK и его SHA-256 указаны в отчёте этапа 2. На Huawei требуется ручная проверка шести ярлыков, пальца, ушей, нижнего края и ореолов. Adaptive v2 остаётся кандидатом; проверка на устройстве не выполнялась.

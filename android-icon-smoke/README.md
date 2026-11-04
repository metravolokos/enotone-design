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

Получен только `00_android_smoke_code.zip` (SHA-256 `fff4134202f182894dcb507d0a425d3d2c4207a8a3d0ecad6b861e31b1a771ec`). В проекте находятся производные PNG-ресурсы APK, а не полный комплект художественных оригиналов. `python3 tools/verify_enotone_assets.py --smoke-only` из корня проверяет 22 PNG и шесть alias. `RESOURCES.sha256` фиксирует точные байты PNG из входного ZIP. Проверка без флага остаётся строгой: все 37 файлов пока не проверены, требуются остальные семь архивов.

GitHub Actions собирает APK и выполняет lint, artifact `enotone-icon-smoke-debug-apk` содержит APK и его SHA-256. На Huawei требуется ручная проверка шести ярлыков, пальца, ушей, нижнего края и ореолов. Adaptive v2 остаётся кандидатом; проверка на устройстве не выполнялась.

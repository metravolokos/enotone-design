# Локальная сборка — запасной APK

APK собран в опубликованной среде из коммита `62245b71beffb26c244e9a408bfe7d40f864af1b` командой `gradle --offline --no-daemon :app:assembleDebug`. Debug-подпись проверена. Это **не** artifact GitHub Actions.

[Актуальный GitHub Actions run после перехода на строгую проверку — [41885391094](https://github.com/metravolokos/enotone-design/actions/runs/41885391094) — завершился до первого шага; job steps и artifacts пусты, скачивание логов возвращает `BlobNotFound`. Точная причина отказа runner из доступных данных неизвестна. Свежая локальная сборка описана в [`docs/ANDROID_SMOKE_STAGE2.md`](../../docs/ANDROID_SMOKE_STAGE2.md), но этот APK не стал Actions artifact.

Сохранённый fallback APK можно скачать как [файл репозитория](enotone-icon-smoke-debug.apk); он собран раньше и отличается от свежего локального APK. Подпись debug, установка только вручную; ADB не используется. SHA-256 — в соседнем `.apk.sha256`. Исходники этапа 2 импортированы, строгая проверка 37 файлов прошла.

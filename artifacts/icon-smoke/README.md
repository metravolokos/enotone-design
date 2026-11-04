# Локальная сборка — запасной APK

APK собран в опубликованной среде из коммита `62245b71beffb26c244e9a408bfe7d40f864af1b` командой `gradle --offline --no-daemon :app:assembleDebug`. Debug-подпись проверена. Это **не** artifact GitHub Actions.

[GitHub Actions run](https://github.com/metravolokos/enotone-design/actions/runs/41833315217) завершился ошибкой до первого шага, в том числе после повторного запуска; runner не назначен, logs не созданы, artifacts пуст. Причина в annotations недоступна через подключённый API-инструмент; потребуется открыть страницу run и проверить сообщение GitHub. Успешная CI-сборка и CI lint пока не подтверждены.

Для скачивания откройте APK в GitHub и нажмите Download raw file. Подпись debug, установка только вручную; ADB не используется. SHA-256 — в соседнем `.apk.sha256`. Оригиналы и полная проверка 37 файлов ожидают этапа 2.

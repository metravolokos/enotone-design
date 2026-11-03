# Перенос утверждённых графических ресурсов

**Состояние:** документация сохранена в GitHub; исходные PNG/JPG должны быть добавлены отдельно.

## Источник

Архив `enoTone-assets-upload.zip` из чата разработки, содержащий **12 файлов** внутри папки `assets/`.

- `assets/references/bandit-10-approved.png` — исходный выбранный коллаж 10 сцен;
- `assets/references/ui-palette-approved.jpg` — утверждённая палитра;
- `assets/icons/originals/four-icon-board.png` — четыре утверждённые иконки;
- `assets/icons/exports/` — восемь PNG (432 и 512 px);
- `assets/icons/preview/icon-review.png` — обзор.

## Загрузка через GitHub

1. Распаковать `enoTone-assets-upload.zip`; **не** загружать только ZIP-файл вместо изображений.
2. В корне репозитория GitHub открыть **Add file → Upload files**.
3. Перетащить **папку `assets` целиком** из распакованного архива в область загрузки.
4. Проверить сохранение путей `assets/references/`, `assets/icons/originals/`, `assets/icons/exports/`, `assets/icons/preview/`.
5. Подтвердить коммит с сообщением `assets: import approved mascot and application icons`.

После загрузки сверить 12 путей с `docs/SOURCES.sha256` и убедиться, что референсы и иконки визуально совпадают. Картинки повторно не генерировать и не менять.

**Рабочие проекты AllMusic не изменять.**

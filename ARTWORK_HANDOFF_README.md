# enoTone · временная передача утверждённых исходников

Эта ветка **не предназначена для слияния** в `main` и **не является заменой** Draft PR #4. Она нужна только, чтобы обойти проблему с вложениями Codex Cloud.

## Какие файлы загрузить вручную через GitHub

Откройте [страницу загрузки именно в эту ветку](https://github.com/metravolokos/enotone-design/upload/enotone-artwork-handoff-20261104) и загрузите в корень ветки:

- `01_enotone_artwork_A.zip` — SHA-256 `9844566dfd5e883554e6323ccae85aa2231aa296134ed7d204f435c0e10f22cd`
- `02_enotone_artwork_B.zip` — SHA-256 `b14f28a94ca3e26bd9f891572a176a63da7a4bdb9d65db35a977501b92c21519`

Выбрать **Commit changes directly to the enotone-artwork-handoff-20261104 branch**, не `main`.

Оба файла суммарно содержат актуальные ресурсы из семи архивов 01–07: 4 утверждённые иконки, 13 сцен Бандита, 10 UI референсов, палитру, wordmark и манифесты. По независимой локальной проверке с `00_android_smoke_code.zip`: 75 уникальных файлов, `python3 tools/verify_enotone_assets.py` — **37/37 SHA-256, 6 launcher alias, XML OK**.

## Указания Codex Cloud

Работать в текущем PR #4, без нового PR и без merge этой ветки:
```bash
git fetch origin enotone-artwork-handoff-20261104
git show FETCH_HEAD:01_enotone_artwork_A.zip > /tmp/01_enotone_artwork_A.zip
git show FETCH_HEAD:02_enotone_artwork_B.zip > /tmp/02_enotone_artwork_B.zip
sha256sum /tmp/0?_enotone_artwork_?.zip
unzip -n /tmp/01_enotone_artwork_A.zip -d .
unzip -n /tmp/02_enotone_artwork_B.zip -d .
python3 tools/verify_enotone_assets.py
```

Прежде чем запускать эти команды, убедиться что **оба ZIP уже добавлены в handoff branch**; если нет — ничего не подменять. Затем пересобрать debug APK, обновить **существующий** Draft PR #4. Не изменять утверждённые изображения, `main`, другие репозитории; не использовать ADB. После независимой приёмки можно удалить временную ветку, не затрагивая историю PR.

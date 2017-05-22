# Блог для технотрека

### Heroku
[![Heroku](https://heroku-badge.herokuapp.com/?app=track-mail-web-kosolapov)](https://track-mail-web-kosolapov.herokuapp.com)

### Работа
Запуск двух gunicorn (ищет конфиги в ../conf/gunicorn-1.conf,
../conf/gunicorn-2.conf)
```bash
$ foreman start -f Procfile.dev
```
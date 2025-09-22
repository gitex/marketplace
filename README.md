### Инициализация

#### Pypi

Для работы локального pypi необходимо задать пользователя и пароль командой:
```bash
# вариант 1 (Linux): утилита htpasswd
sudo apt install apache2-utils
htpasswd -B -C 10 -c pypi-data/.htpasswd user
# вариант 2 (через контейнер):
docker run --rm -it xmartlabs/htpasswd -B -C 10 user > pypi-data/.htpasswd
```
где `user` - это пользователь 

Переменные `user` и `password` нужно добавить в `./infra/env/.local_pypi.env`.

Далее, они будут использоваться для синхронизации с core.


## Старт

```
git clone https://github.com/a-berezhkov/django_auth.git

python -m venv .venv

source .venv/bin/activate

pip install Django

cd config

python manage.py migrate

```

## Endpoints

- `/admin` - админка
- `/account/` - все пользователи
- `/account/register` - регистрация пользователя
- `/account/login` - авторизация пользователя
- `/account/logout` - выход пользователя
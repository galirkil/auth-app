# auth-app

Django приложение для аутентификации пользователя с использованием JWT-токенов.

## Стек

- Python
- Django
- DRF
- Simple JWT
- drf-spectacular
- Faker (для тестов)

## Запуск проекта

Клонируйте репозиторий:

```bash
git clone git@github.com:galirkil/auth-app.git
```

Перейдите в папку с проектом, установите и активируйте виртуальное окружение:

```bash
cd auth-app
python3 -m venv venv
source venv/bin/activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Выполните миграции:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Создайте суперпользователя:

```bash
python3 manage.py createsuperuser
```

Запустите сервер:

```bash
python3 manage.py runserver
```

## Запуск тестов

```bash
python3 manage.py test
```

## Документация API

Документация API приложения доступна по ссылке - http://localhost:8000/docs/

## Предложения по улучшению

- Дополнить документацию API примерами ответов сервера для случаев неуспешного
  выполнения запросов

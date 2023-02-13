[![Python Linting](https://github.com/F0RRZZ/django-homework/actions/workflows/python-linting-tests.yml/badge.svg)](https://github.com/F0RRZZ/django-homework/actions/workflows/python-linting-tests.yml)
[![Checking with mypy](https://github.com/F0RRZZ/django-homework/actions/workflows/mypy-tests.yml/badge.svg)](https://github.com/F0RRZZ/django-homework/actions/workflows/mypy-tests.yml)
[![Django CI](https://github.com/F0RRZZ/django-homework/actions/workflows/django-tests.yml/badge.svg)](https://github.com/F0RRZZ/django-homework/actions/workflows/django-tests.yml)

# django-homework
---

#### ! Для того, чтобы проделать представленные шаги на Windows, необходимо установить git bash!
[Git Bash](https://gitforwindows.org/)

---

1. Клонируем репозиторий

```shell
git clone https://github.com/F0RRZZ/django-homework.git
```

---

2. Создаем и активируем venv

Windows:
```shell
cd django-homework
python -m venv venv
source venv/Scripts/activate
```


Linux/MacOS:

```shell
cd django-homework
python3 -m venv venv
source venv/bin/activate
```

---

3. Устанавливаем зависимости
---
* Основные зависимости:

Windows:

```shell
pip install -r requirements.txt
```

Linux/MacOS:

```shell
pip3 install -r requirements.txt
```

---
* Зависимости для разработки

Windows:

```shell
pip install -r requirements-dev.txt
```

Linux/MacOS:

```shell
pip3 install -r requirements-dev.txt
```

---
* Зависимости для тестов

Windows:

```shell
pip install -r requirements-test.txt
```

Linux/MacOS:

```shell
pip3 install -r requirements-test.txt
```

---

4. Переменные окружения

Чтобы создать и отредактировать переменные окружения, сначала пройдите по пути:

```shell
cd homework/
```

В данной директории находится тестовый .env (.env.example)
Чтобы создать .env, введите команду:

```shell
cp .env.example .env
```

Готово. Теперь в этой директории находится .env, который можно отредактировать
при необходимости.

Чтобы перейти к следующему шагу, поднимитесь на уровень выше

```shell
cd ..
```

---

5. Запускаем сервер

Windows:
```shell
python manage.py runserver
```
Linux/MacOS:
```shell
python3 manage.py runserver
```

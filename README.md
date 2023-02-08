# django-homework
---

#### ! Для того, чтобы проделать представленные шаги на Windows, необходимо установить git bash!

---

1. Клонируем репозиторий

```
git clone https://github.com/F0RRZZ/django-homework.git
```

---

2. Создаем и активируем venv

Windows:
```
cd django-homework
python -m venv venv
source venv/Scripts/activate
```


Linux/MacOS:

```
cd django-homework
python3 -m venv venv
source venv/bin/activate
```

---

3. Устанавливаем зависимости
---
* Основные зависимости:

Windows:

```
pip install -r requirements.txt
```

Linux/MacOS:

```
pip3 install -r requirements.txt
```

---
* Зависимости для разработки

Windows:

```
pip install -r requirements-dev.txt
```

Linux/MacOS:

```
pip3 install -r requirements-dev.txt
```

---
* Зависимости для тестов

Windows:

```
pip install -r requirements-dev.txt
```

Linux/MacOS:

```
pip3 install -r requirements-dev.txt
```


---
4. Переменные окружения (secret key)

Чтобы создать и отредактировать переменные окружения, сначала пройдите по пути:

```shell
cd homework/homework
```

В данной директории находится тестовый .env (.env.example)
Чтобы создать .env, введите команду:

```shell
cp .env.example .env
```

Готово. Теперь в этой директории находится .env, который можно отредактировать
при необходимости.

---

5. Запускаем сервер

Windows:
```
cd homework
python manage.py runserver
```
Linux/MacOS:
```
cd homework
python3 manage.py runserver
```

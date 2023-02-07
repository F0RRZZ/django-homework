# django-homework
## Запуск в dev-режиме

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

Windows:

```
pip install -r requirements.txt
```

Linux/MacOS:

```
pip3 install -r requirements.txt
```

---

4. Запускаем сервер

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

### Установка:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:andrew12022/bookstore_django.git
```

```
cd bookstore_django
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

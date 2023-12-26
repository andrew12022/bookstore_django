# BookStore

**BookStore** — это проект книжного магазина, где пользователи могут просматривать книги.

## Функции

- Просмотр информации о различных книгах.
- Получение информации об акциях и компании.
- Добавление новых книг через специальную форму.
  
## Установка:

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

## Технологии и необходимые инструменты
- Python 3.9
- Django 3.2.16
- pytest
- sqlite3
- django-debug-toolbar

## Автор
- [Андрей Елистратов](https://github.com/andrew12022)

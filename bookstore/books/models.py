from django.db import models


class Category (models.Model):
    title = models.CharField(
        'Название',
        max_length=256,
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text=('Идентификатор страницы для URL; '
                   'разрешены символы латиницы, '
                   'цифры, дефис и подчёркивание.'),
    )
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть категорию.',
    )

    class Meta:
        verbose_name = 'объект «Категория»'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Author (models.Model):
    name = models.CharField(
        'Имя автора',
        max_length=256,
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text=('Идентификатор страницы для URL; '
                   'разрешены символы латиницы, '
                   'цифры, дефис и подчёркивание.'),
    )

    class Meta:
        verbose_name = 'объект «Автор»'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Publisher (models.Model):
    title = models.CharField(
        'Название',
        max_length=256,
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text=('Идентификатор страницы для URL; '
                   'разрешены символы латиницы, '
                   'цифры, дефис и подчёркивание.'),
    )

    class Meta:
        verbose_name = 'объект «Издательство»'
        verbose_name_plural = 'Издательства'

    def __str__(self):
        return self.title


class Book (models.Model):
    title = models.CharField(
        'Название',
        max_length=256,
    )
    description = models.TextField(
        'Описание',
    )
    price = models.IntegerField(
        'Цена',
    )
    count_of_pages = models.IntegerField(
        'Количество страниц',
    )
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть книгу.',
    )
    image = models.ImageField(
        'Картинка',
        upload_to='books_images',
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='books',
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор',
        related_name='books',
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Издательство',
        related_name='books',
    )

    class Meta:
        verbose_name = 'объект «Книга»'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

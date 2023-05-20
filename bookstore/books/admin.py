from django.contrib import admin

from books.models import Author, Book, Category, Publisher

admin.site.empty_value_display = 'Не задано'


class BookInline(admin.StackedInline):
    model = Book
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'price',
        'count_of_pages',
        'is_published',
        'category',
        'author',
        'publisher',
    )
    list_editable = (
        'is_published',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'category',
        'author',
        'publisher',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    inlines = (
        BookInline,
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    inlines = (
        BookInline,
    )


class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    inlines = (
        BookInline,
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)

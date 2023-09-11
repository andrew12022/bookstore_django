from django import forms

from books.models import Book


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
        self.fields['author'].empty_label = 'Автор не выбран'
        self.fields['publisher'].empty_label = 'Издательство не выбрано'

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 3, })
        }

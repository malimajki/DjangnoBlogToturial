from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category']
        labels = {
            'title': 'Název článku',
            'body': 'Obsah článku',
            'category': 'Kategorie'
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        labels = {
            'title':'Název kategorie'
        }

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
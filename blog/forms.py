from django import forms
from .models import Post, Category, Comment

#choices = [('sports', 'sports'), ('tech','tech'),  ('entertainment', 'entertainment')]
choices = Category.objects.all().values_list('name', 'name')
choice_list =[]

for item in choices:
    choice_list.append (item)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'category', 'author', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id': 'author', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'rows': 5}),
        }

class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'category', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }
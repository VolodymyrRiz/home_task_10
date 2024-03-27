from django.forms import CharField, TextInput, EmailField, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class TagForm(UserCreationForm):
    user = CharField(max_length=19, required=True, widget=TextInput(attrs={"class": "form-control", }))
    name = CharField(max_length=25, required=True, widget=TextInput(attrs={"class": "form-control", }))
    
    class Meta:
        model = User
        fields = ("user", "name")


class QuoteForm(forms.Form):
    quote = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    tags = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))  # Assuming tags are entered as a comma-separated string
    author = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    def clean_tags(self):
        tags_str = self.cleaned_data['tags']
        tags = [tag.strip() for tag in tags_str.split(',')]
        return tags




# class QuoteForm(AuthenticationForm):
#     quote = CharField(widget=TextInput(attrs={"class": "form-control"}))
#     tags = ListField(widget=ArraysInput(attrs={"class": "form-control"}))
#     author = CharField(widget=TextInput(attrs={"class": "form-control"}))

#     class Meta:
#         model = User
#         fields = ['quote', 'tags', 'author']
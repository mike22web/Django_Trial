from django.http import HttpResponse
from django.shortcuts import render
from django import forms


def about(request):
    return render(request, 'about.html', {'gretting': 'Hello'})


class UserForm(forms.Form):
    # name = forms.CharField(label="Имя")
    comment = forms.CharField(label="", widget=forms.Textarea)


comment_form = UserForm


def home(request):
    return render(request, 'home.html', {'text_area': comment_form})

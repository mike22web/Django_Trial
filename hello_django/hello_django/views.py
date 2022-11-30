from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'about.html', {'gretting':'Hello'})


def home(request):
    return HttpResponse('This is home page!!!')



from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>I'm from frist app</h1>")

def test(request):
    return HttpResponse("<h1>I'm from test page </h1>")

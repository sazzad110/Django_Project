from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>This is home page</h1> <a href='contact/'> Contact </a> <a href='about/'> About </a> ")

def contact(request):
    return HttpResponse("<h1>This is contact page</h1> <a href='/'> Home </a> <a href='/about/'> About </a>")

def about(request):
    return HttpResponse("<h1>This is about page</h1> <a href='/'> Home </a> <a href='/contact/'> Contact </a>")

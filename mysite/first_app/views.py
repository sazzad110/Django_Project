from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    diction = {"text_1": "Sending value from view"}     # to show this in index.html
    return render(request,'first_app/index.html',context=diction)
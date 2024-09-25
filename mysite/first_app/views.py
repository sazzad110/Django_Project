from django.shortcuts import render,redirect
from django.http import HttpResponse
from first_app.models import Muscian,Album            # i want to show all musician from my database
from first_app.forms import UserForm 

def index(request):
    
    return HttpResponse("Hello World")

def form(request):
    form_obj = UserForm()   # create obj of my form
    dict = {'test_form':form_obj}       # to pass this form in my html page
    return render(request,'first_app/index.html',context=dict)

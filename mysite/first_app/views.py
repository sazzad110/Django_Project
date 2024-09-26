from django.shortcuts import render,redirect
from django.http import HttpResponse
from first_app.models import Muscian,Album            # i want to show all musician from my database
from first_app.forms import UserForm 

def index(request):
    
    return HttpResponse("Hello World")

def form(request):
    form_obj = UserForm()   # create obj of my form to store an empty form
    dict = {'test_form':form_obj}       # to pass this form in my html page

    # if anyone click submit then POST mehtod check
    if request.method == 'POST':
        form_obj = UserForm(request.POST)   # to get submitted information

        if form_obj.is_valid():
            user_name = form_obj.cleaned_data['name']
            user_email = form_obj.cleaned_data['email']
            user_dob = form_obj.cleaned_data['user_dob']

            dict.update({'user_name':user_name})
            dict.update({'user_email':user_email})
            dict.update({'user_dob':user_dob})
            dict.update({'is_submitted':'yes'})

    return render(request,'first_app/index.html',context=dict)

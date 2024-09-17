from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Muscian,Album            # i want to show all musician from my database

def index(request):
    musician_list = Muscian.objects.order_by('first_name')
    diction = {
        "text_1":"List of Musician",
        "musician":musician_list
    }
    return render(request,'first_app/index.html',context=diction)
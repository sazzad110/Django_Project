from django.shortcuts import render,redirect
from django.http import HttpResponse
from first_app.models import Muscian,Album            # i want to show all musician from my database
from first_app.forms import MusicianForm

def index(request):
    musician_list = Muscian.objects.order_by('first_name')

    if  request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the same page to see the updated list
    else:
        form = MusicianForm()

    diction = {
        "text_1":"List of Musician",
        "musician":musician_list,
        "form":form
    }
    return render(request,'first_app/index.html',context=diction)
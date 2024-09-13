from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name="polls"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about"),
]
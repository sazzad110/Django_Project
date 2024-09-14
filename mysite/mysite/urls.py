from django.contrib import admin
from django.urls import path
from polls import views
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/",include("polls.urls"))

]
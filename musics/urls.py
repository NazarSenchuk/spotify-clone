
from django.urls import path
from . import views

app_name='musics'

urlpatterns = [
path('',views.home , name= "home_page"),
path('add/', views.create, name ="add")
   
]

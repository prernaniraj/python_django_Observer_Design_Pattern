from django.urls import path
from First_app import views

urlpatterns = [
    path('',views.index, name ='index'),
]
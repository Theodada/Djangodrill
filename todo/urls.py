from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.index),
    path('TODOdetail/', views.TODOdetail),
]
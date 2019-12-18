from django.urls import path
from . import views

app_name = 'jar'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics')
]
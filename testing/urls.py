from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start/',views.test,name='test'),
    path('feedback/',views.feedback,name='feedback'),
]
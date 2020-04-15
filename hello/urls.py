from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('getAll', views.GetAll.as_view()),
    path('delete', views.Delete.as_view()),
    path('add', views.Add.as_view()),
    path('change', views.Change.as_view()),
]

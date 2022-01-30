from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('',ListTodoAPIView.as_view()),
    path('create/',CreateTodoAPIView.as_view()),
    path('update/<int:pk>/',UpdateTodoAPIView.as_view()),
    path('delete/<int:pk>/',DeleteTodoAPIView.as_view()),



]
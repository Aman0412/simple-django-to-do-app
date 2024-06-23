from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name="index"),
        path('add/', views.add_task, name="add_task"),
        path('del/<str:id>', views.delete_task, name="delete_task")
]

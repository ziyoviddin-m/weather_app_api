from django.urls import path
from . import views

app_name = 'cities'

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
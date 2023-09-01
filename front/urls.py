from django.urls import path
from . import views

urlpatterns = [
    path('',views.front_index,name='front_index')
]

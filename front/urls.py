from django.urls import path
from . import views

urlpatterns = [
    path('',views.front_index,name='front_index'),
    path('about/us/',views.front_about,name='front_about'),
    path('contact/us/',views.front_contact,name='front_contact'),
]

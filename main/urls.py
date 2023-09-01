from django.urls import path
from . import views

urlpatterns = [
    path('master/settings/site/',views.master_settings,name="master_settings"),
]

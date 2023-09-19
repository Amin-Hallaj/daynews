from django.urls import path
from . import views

urlpatterns = [
    path('master/settings/site/',views.master_settings,name="master_settings"),
    path('master/login/',views.master_login,name="master_login"),
    path('master/login/submit/',views.master_login_submit,name="master_login_submit"),
]

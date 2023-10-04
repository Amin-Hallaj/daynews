from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/post/create/',views.master_dashboard_post_create,name='master_dashboard_post_create'),
    path('dashboard/post/create/submit/',views.master_dashboard_post_create_submit,name='master_dashboard_post_create_submit'),
    path('dashboard/post/edit/<id>/',views.master_dashboard_post_edit,name='master_dashboard_post_edit'),
    path('dashboard/post/edit/submit/<id>/',views.master_dashboard_post_edit_submit,name='master_dashboard_post_edit_submit'),
]
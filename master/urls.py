from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.master_dashboard,name='master_dashboard'),
    path('dashboard/post/list',views.master_dashboard_post_list,name='master_dashboard_post_list'),
    path('dashboard/post/categories/',views.master_dashboard_post_categories,name='master_dashboard_post_categories'),
    path('dashboard/post/create/',views.master_dashboard_post_create,name='master_dashboard_post_create'),
    path('dashboard/post/edit/',views.master_dashboard_post_edit,name='master_dashboard_post_edit'),
    path('dashboard/author/list/',views.master_dashboard_author_list,name='master_dashboard_author_list'),
    path('dashboard/author/single/',views.master_dashboard_author_single,name='master_dashboard_author_single'),
    path('dashboard/edit/profile/',views.master_dashboard_edit_profile,name='master_dashboard_edit_profile'),
    path('dashboard/reviews/',views.master_dashboard_reviews,name='master_dashboard_reviews'),
    path('dashboard/settings/',views.master_dashboard_settings,name='master_dashboard_settings'),
]
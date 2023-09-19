from django.urls import path
from . import views

urlpatterns = [
    path('',views.front_index,name='front_index'),
    path('about/us/',views.front_about,name='front_about'),
    path('contact/us/',views.front_contact,name='front_contact'),
    path('author/',views.front_author,name='front_author'),
    path('categories/',views.front_categories,name='front_categories'),
    path('post/list/',views.front_post_list,name='front_post_list'),
    path('post/single/',views.front_post_single,name='front_post_single'),
    path('search/result/',views.front_search_result,name='front_search_result'),
    path('signin/',views.front_signin,name='front_signin'),
    path('signup/',views.front_signup,name='front_signup'),
    path('tag/',views.front_tag,name='front_tag'),
    path('404/',views.front_404,name='front_404'),
]

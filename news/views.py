import time
from django.shortcuts import render , redirect , get_object_or_404
from django.http import JsonResponse
from main.models import Main
from news.models import News


def master_dashboard_post_create(request):
    return render(request,'master/dashboard-post-create.html',{})


def master_dashboard_post_create_submit(request):

    if request.method=='POST':
        news_titel=request.POST.get('news_titel')
        news_brief=request.POST.get('news_brief')
        news_text=request.POST.get('news_text')

        News.objects.create(
            writer=request.user,
            title=news_titel,
            news_brief=news_brief,
            news_text=news_text,
            news_date=time.time(),
        )

        
    return redirect("master_dashboard_post_list")



def master_dashboard_post_edit(request):
    return render(request,'master/dashboard-post-edit.html',{})
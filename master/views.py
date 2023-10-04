from django.shortcuts import render , redirect , get_object_or_404
from main.models import Main
from news.models import News
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


def master_dashboard(request):
    return render(request,'master/dashboard.html',{})


def master_dashboard_post_list(request):

    list_news=News.objects.all().order_by('-pk')

    return render(request,'master/dashboard-post-list.html',{'list_news':list_news})


def master_dashboard_post_categories(request):
    return render(request,'master/dashboard-post-categories.html',{})


def master_dashboard_edit_profile(request):
    return render(request,'master/dashboard-edit-profile.html',{})


def master_dashboard_author_list(request):
    return render(request,'master/dashboard-author-list.html',{})


def master_dashboard_author_single(request):
    return render(request,'master/dashboard-author-single.html',{})


def master_dashboard_reviews(request):
    return render(request,'master/dashboard-reviews.html',{})


def master_dashboard_settings(request):
    return render(request,'master/dashboard-settings.html',{})


def master_news_delete(request,id):

    try:
        news_delete = News.objects.get(id=id)
        fs=FileSystemStorage()
        fs.delete(news_delete.picname)
        news_delete.delete()

        messages.success(request, 'حذف با موفقیت انجام شد')
    except:
        messages.error(request, 'حذف با موفقیت انجام نشد')

    return redirect("master_dashboard_post_list")
import time
from django.shortcuts import render , redirect , get_object_or_404
from django.http import JsonResponse
from main.func.public import upload_files
from django.contrib import messages
from main.models import Main
from news.models import News


def master_dashboard_post_create(request):
    return render(request,'master/dashboard-post-create.html',{})


def master_dashboard_post_create_submit(request):

    if request.method=='POST':
        news_titel=request.POST.get('news_titel')
        news_brief=request.POST.get('news_brief')
        news_text=request.POST.get('news_text')
        
        if news_titel == "" or news_brief == "" or news_text == "" :
            messages.error(request, 'لطفا تمامی فیلد ها را پر کنید')
            return redirect("master_dashboard_post_create")
        
        else:
            image_news = request.FILES.get('image_news')
            if image_news is not None:
                url,filename,error,msg,type = upload_files(image_news , "images_news/")

                if error:
                    messages.error(request,msg)
                    return redirect("master_dashboard_post_create") 

            else:
                url = filename = None

            News.objects.create(
                writer=request.user,
                title=news_titel,
                news_brief=news_brief,
                news_text=news_text,
                picname=filename,
                picurl=url,
                news_date=time.time(),
            )
        
    return redirect("master_dashboard_post_list")



def master_dashboard_post_edit(request):
    return render(request,'master/dashboard-post-edit.html',{})
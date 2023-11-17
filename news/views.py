import time
from django.shortcuts import render , redirect , get_object_or_404
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from main.func.public import upload_files
from django.contrib import messages
from main.models import Main
from news.models import News,Category,SubCategory


def master_dashboard_post_create(request):

    category_news=News.objects.all()

    return render(request,'master/dashboard-post-create.html',{'category_news':category_news})


def master_dashboard_post_create_submit(request):

    if request.method=='POST':
        news_titel=request.POST.get('news_titel')
        news_brief=request.POST.get('news_brief')
        news_text=request.POST.get('news_text')
        news_category=request.POST.get('news_category')
        important=request.POST.get('important') == 'on'
        
        if news_titel == "" or news_brief == "" or news_text == "" or important == "" :
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
                news_subcategory=news_category,
                important=important,
            )
        
    return redirect("master_dashboard_post_list")



def master_dashboard_post_edit(request,id):

    news_edits=News.objects.get(id=id)

    return render(request,'master/dashboard-post-edit.html',{'id':id,'news_edits':news_edits})


def master_dashboard_post_edit_submit(request,id):

    # news_edits=News.objects.get(title=word)


    if request.method=='POST':
        title_edit=request.POST.get('title_edit')
        news_brief_edit=request.POST.get('news_brief_edit')
        news_text_edit=request.POST.get('news_text_edit')
        
        if title_edit == "" or news_brief_edit == "" or news_text_edit == "" :
            messages.error(request, 'لطفا تمامی فیلد ها را پر کنید')
            return redirect("master_dashboard_post_edit", id=id)
        
        try:
            image_news = request.FILES.get('image_news')
            url,filename,error,msg,type = upload_files(image_news , "images_news/")

            if error:
                messages.error(request,msg)

                news_edit=News.objects.get(id=id)

                fss = FileSystemStorage()
                if news_edit.picname is not None and news_edit.picname != "":
                    fss.delete(news_edit.picname)
                news_edit.title=title_edit
                news_edit.news_brief=news_brief_edit
                news_edit.news_text=news_text_edit
                news_edit.picname=filename
                news_edit.picurl=url
                news_edit.news_date=time.time(),
                news_edit.save()
            
        except:
            news_edit=News.objects.get(id=id)

            news_edit.title=title_edit
            news_edit.news_brief=news_brief_edit
            news_edit.news_text=news_text_edit
            # news_edit.news_date=time.time(),
            news_edit.save()

    return redirect("master_dashboard_post_edit", id=id)
from django.shortcuts import render , redirect , get_object_or_404
from main.models import Main
from news.models import News


def front_index(request):

    site_head=Main.objects.get()
    show_news=News.objects.all().order_by('-pk')

    return render(request,'front/index.html',{'show_news':show_news , "site_head":site_head})


def front_about(request):
    return render(request,'front/about-us.html',{})


def front_contact(request):
    return render(request,'front/contact-us.html',{})


def front_author(request):
    return render(request,'front/author.html',{})


def front_categories(request):
    return render(request,'front/categories.html',{})


def front_post_list(request):
    return render(request,'front/post-list.html',{})


def front_post_single(request,word):

    post_single=News.objects.get(title=word)
    
    return render(request,'front/post-single.html',{'post_single':post_single,'word':word})


def front_search_result(request):
    return render(request,'front/search-result.html',{})


def front_signin(request):
    return render(request,'front/signin.html',{})


def front_signup(request):
    return render(request,'front/signup.html',{})


def front_tag(request):
    return render(request,'front/tag.html',{})


def front_404(request):
    return render(request,'front/404.html',{})
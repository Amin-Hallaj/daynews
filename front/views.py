from django.shortcuts import render , redirect , get_object_or_404


def front_index(request):
    return render(request,'front/index.html',{})


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


def front_post_single(request):
    return render(request,'front/post-single.html',{})


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
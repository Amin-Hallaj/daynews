from django.shortcuts import render , redirect , get_object_or_404


def front_index(request):
    return render(request,'front/index.html',{})


def front_about(request):
    return render(request,'front/about-us.html',{})


def front_contact(request):
    return render(request,'front/contact-us.html',{})
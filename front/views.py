from django.shortcuts import render , redirect , get_object_or_404


def front_index(request):
    return render(request,'front/index.html',{})

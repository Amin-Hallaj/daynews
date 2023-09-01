from django.shortcuts import render , redirect , get_object_or_404


def master_settings(request):
    return render(request,'master/settings.html',{})

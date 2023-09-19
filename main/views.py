from django.shortcuts import render , redirect , get_object_or_404


def master_settings(request):
    return render(request,'master/settings.html',{})


def master_login(request):
    return render(request,'master/login.html',{})


def master_login_submit(request):
    return redirect('master_login')


def master_logout(request):
    return redirect('master_login')

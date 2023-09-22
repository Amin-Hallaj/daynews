from django.shortcuts import render , redirect , get_object_or_404


def master_dashboard(request):
    return render(request,'master/dashboard.html',{})


def master_dashboard_post_list(request):
    return render(request,'master/dashboard-post-list.html',{})


def master_dashboard_post_categories(request):
    return render(request,'master/dashboard-post-categories.html',{})


def master_dashboard_edit_profile(request):
    return render(request,'master/dashboard-edit-profile.html',{})


def master_dashboard_post_create(request):
    return render(request,'master/dashboard-post-create.html',{})


def master_dashboard_author_list(request):
    return render(request,'master/dashboard-author-list.html',{})


def master_dashboard_author_single(request):
    return render(request,'master/dashboard-author-single.html',{})


def master_dashboard_post_edit(request):
    return render(request,'master/dashboard-post-edit.html',{})


def master_dashboard_reviews(request):
    return render(request,'master/dashboard-reviews.html',{})


def master_dashboard_settings(request):
    return render(request,'master/dashboard-settings.html',{})
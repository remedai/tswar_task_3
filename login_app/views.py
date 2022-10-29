from django.http.response import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def render_login(request):
    return render(request,"login.html")

    # def perform_login(request):
        # if request.method !="POST":
        #     return HttpResponse("Method not Allowed")
        # else:
        #     username=request.POST.get("username")
        #     password=request.POST.get("password")
        #     user_obj=authenticate(request,username=username,password=password)
            
        #     if user_obj is not None:
        #         login(request,user_obj)
        #         return HttpResponseRedirect(reverse("admin_dashbord"))
        #     else: 
        #         return HttpResponseRedirect("/")
def perform_login(request):
    if request.method !="POST":
        return HttpResponse("Method not Allowed")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(request,username=username,password=password)
        if user_obj is not None:
            login(request,user_obj)
            return HttpResponseRedirect(reverse("admine_dashboard"))
        else:
            messages.error(request,"username or password is not Invalid") 
            return HttpResponseRedirect("/")

def admine_dashboard(request):
    return render(request, "admin_dashboard.html")

def perform_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

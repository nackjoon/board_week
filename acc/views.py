from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.urls.conf import include
from .models import User

# Create your views here.
def index(request):
    return render(request,'acc/index.html')

def userlogin(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        #print(authenticate(username=un, password=pw))
        user = authenticate(username=un, password=pw)
        if user:
            login(request,user)
            #print(dir(request))
    return redirect('acc:index')

def userJoin(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        cm = request.POST.get("comment")
        pc = request.FILES.get("pic")
        User.objects.create_user(username=un,password=pw,comment=cm,pic=pc)
        return redirect("acc:index")
    return render(request,"acc/member/userJoin.html")

def userLogout(request):
    logout(request)
    return redirect("acc:index")

def userInfo(request):
    return render(request,"acc/member/userInfo.html")

def userUpdate(request):
    if request.method == "POST":
        un = request.user.username
        pw = request.POST.get("password")
        pc = request.FILES.get("pic")
        cm = request.POST.get("comment")
        u = User.objects.get(username=un)
        if pw:
            u.set_password(pw)
        if pc:
            u.pic=pc
        u.comment=cm
        u.save()
        user = authenticate(username=un,password=pw)
        login(request,user)
        return redirect("acc:userInfo")
    return redirect("acc:index")

def userDel(request):
    u = User.objects.get(username=request.user.username)
    u.delete()
    return redirect("acc:index")
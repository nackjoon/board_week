from django.shortcuts import render,redirect
from .models import Board
from acc.models import User
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.
def index(request):

    page = request.GET.get('page',1)
    cate = request.GET.get('cate','')
    kw = request.GET.get('kw','')

    if kw:
        if cate == "sub":
            b = Board.objects.filter(subject__startswith=kw).order_by("-ctime")
        elif cate == "wri":
            b = Board.objects.filter(writer=kw).order_by("-ctime")
        elif cate == "con":
            b = Board.objects.filter(content__contains=kw).order_by("-ctime")
    else:
        b = Board.objects.all()

    #b = Board.objects.all()
    pag = Paginator(b,10)
    obj = pag.get_page(page)

    context = {
        "blist" : obj,
        "cate" : cate,
        "kw" : kw
        
    }
    return render(request,"board/index.html",context)

def createBoard(request):

    if request.method == "POST":
        sub = request.POST.get("subject")
        wri = request.user.username
        con = request.POST.get("content")
        Board(subject=sub,writer=wri,content=con,ctime=timezone.now()).save()
        return redirect("board:index")
    return render(request,"board/createBoard.html")

def detail(request,bpk):
    b = Board.objects.get(id=bpk)
    u = User.objects.get(username=b.writer)
    context = {
        "b": b,
        "pic" : u.getpic(),
    }
    return render(request,"board/detail.html",context)

def deleteBoard(request,bpk):
    b = Board.objects.get(id=bpk)
    if(request.user.username == b.writer):
        b.delete()
    else:
        return render(request, "error/forbidden.html")
    return redirect("board:index")

def modifyBoard(request,bpk):
    b=Board.objects.get(id=bpk)
    if request.method == "POST":
        sub = request.POST.get("subject")
        con = request.POST.get("content")
        b.subject = sub
        b.content = con
        if request.user.username == b.writer:
            b.save()
            return redirect('board:detail',bpk=bpk)
        else:
            return render(request, "error/forbidden.html")
    context = {
        "b":b,
    }
    return render(request,"board/modifyBoard.html",context)

def addHeart(request,bpk):
    b = Board.objects.get(id=bpk)
    u = User.objects.get(username=request.user.username)
    b.up.add(u)
    print(b.up)
    return redirect("board:detail",bpk=bpk)

def removeHeart(request,bpk):
    b = Board.objects.get(id=bpk)
    u = User.objects.get(username=request.user.username)
    b.up.remove(u)
    print(b.up)
    return redirect("board:detail",bpk=bpk)
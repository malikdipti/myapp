from django.shortcuts import render,redirect
from .models import Publisher
from .models import Article
from .froms import PublisherForm
from .froms import ArticleForm
from django.contrib import messages



def addPublisher(request):
    pf=PublisherForm()
    return render(request,"addp.html",{"form":pf})

def savePublisher(request):
    name=request.POST.get('name')
    Publisher(name=name).save()
    messages.success(request,"Publisher Added Successfully")
    return redirect('main')


def addArticle(request):
    af=ArticleForm()
    return render(request,"adda.html",{"form":af})


def saveArticle(request):
    name=request.POST.get('name')
    p_name=request.POST.getlist('publisher_name')
    a=Article(name=name)
    a.save()
    a.publisher_name.set(p_name)
    messages.success(request,"Article  Added Successfully")
    return redirect('main')


def viewPublisher(request):
    qs=Publisher.objects.all()
    return render(request,"viewp.html",{"data":qs})


def viewArticle(request):
    qs=Article.objects.all()
    return render(request,"viewa.html",{"data":qs})
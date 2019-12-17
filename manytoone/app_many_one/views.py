from django.shortcuts import render,redirect
from .models import BiriyaniModel
from .models import BiriyaniCatModel
from  .froms import BiriyaniCatFrom
from .froms import BiriyaniForm
from django.contrib import messages


def addBiriyaniCat(request):
    bc=BiriyaniCatFrom()
    return render(request,"addbc.html",{"form":bc})


def saveBiriyaniCat(request):
    bc_name=request.POST.get("b_cat")
    BiriyaniCatModel(b_cat=bc_name).save()
    messages.success(request,"Biriyani category added Successfully")
    return redirect('main')


def addBiriyaniType(request):
    bt=BiriyaniForm()
    return render(request,"addbt.html",{"form":bt})


def saveBiriyaniType(request):
    bt_name=request.POST.get("b_name")
    bt_price=request.POST.get("b_price")
    bt_type=request.POST.get("b_type")
    BiriyaniModel(b_name=bt_name,b_price=bt_price,b_type_id=bt_type).save()
    messages.success(request, "Biriyani added Successfully")
    return redirect('main')


def viewBiriyaniCat(request):
    bcm=BiriyaniCatModel.objects.all()
    return render(request,"viewbc.html" ,{"data":bcm})


def viewBiriyaniType(request):
    bm=BiriyaniModel.objects.all()
    return render(request,"viewbt.html",{"data":bm})
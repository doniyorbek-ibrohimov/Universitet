from http.client import HTTPResponse

from django.shortcuts import render, redirect, get_object_or_404


from main.models import *
from .forms import *
from re import search

def fan_view(request):
    form=FanForm()
    if request.method=="POST":
        form_data=FanForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('fanlar')
        return HTTPResponse(f"{form_data.errors}")
    search_query = request.GET.get('search', '')
    if search_query:
        fanlar = Fan.objects.filter(nom__icontains=search_query)
    else:
        fanlar = Fan.objects.all()
    context = {
        'fanlar': fanlar,
        'search_param': search_query,
        'yonalishlar':Yonalish.objects.all(),
        'form':form
    }
    return render(request, 'fanlar.html', context)

def fan_update(request,pk):
    fan=get_object_or_404(Fan,pk=pk)
    if request.method=="POST":
        fan.nom=request.POST.get('nom')
        fan.assosiy=request.POST.get('assosiy')
        fan.yonalish=Yonalish.objects.get(id=request.POST.get('yonalish'))
        fan.save()
        return redirect('fanlar')
    context={
        'fan':fan,
        'yonalishlar':Yonalish.objects.all()
    }
    return render(request,'fan-update.html',context)

def fan_delete(request,fan_id):
    fan=Fan.objects.get(id=fan_id)
    fan.delete()
    return redirect('admin_site')

def yonalish_delete(request,yonalish_id):
    fan=Yonalish.objects.get(id=yonalish_id)
    fan.delete()
    return redirect('admin_site')


def yonalishlar_view(request):
    form=YonalishForm()
    if request.method=="POST":
        form_data=YonalishForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('yonalishlar')
        return HTTPResponse(f"{form_data.errors}")
    yonalishlar=Yonalish.objects.all()
    context={
        'yonalishlar': yonalishlar,
        'form':form
    }
    return render(request,'yonalishlar.html',context)


def yonalish_update(request,pk):
    yonalish=get_object_or_404(Yonalish,pk=pk)
    if request.method=="POST":
        yonalish.nom=request.POST.get('nom')
        yonalish.aktiv=request.POST.get('aktiv')
        yonalish.save()
        return redirect('yonalishlar')
    context={
        'yonalish':yonalish
    }
    return render(request,'yonalish-update.html',context)


def ustoz_view(request):
    if request.method=="POST":
        form_data=UstozForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('fanlar')
        return HTTPResponse(f"{form_data.errors}")
    search_query = request.GET.get('search', '')
    if search_query:
        ustozlar = Ustoz.objects.filter(ism__icontains=search_query)
    else:
        ustozlar = Ustoz.objects.all()
    context = {
        'ustozlar': ustozlar,
        'search_param': search_query,
        'form':UstozForm
    }
    return render(request, 'ustozlar.html', context)

def ustoz_update(request,pk):
    ustoz=get_object_or_404(Ustoz,pk=pk)
    if request.method=="POST":
        ustoz.ism=request.POST.get('ism')
        ustoz.yosh=request.POST.get('yosh') if request.POST.get('yosh') else None
        ustoz.jins=request.POST.get('jins')
        ustoz.daraja=request.POST.get('daraja')
        ustoz.fan=Yonalish.objects.get(id=request.POST.get('fan'))
        ustoz.save()
        return redirect('ustozlar')
    context={
        'ustoz':ustoz,
        'fanlar':Fan.objects.all()
    }
    return render(request,'ustoz-update.html',context)

def ustoz_delete(request,ustoz_id):
    fan=Ustoz.objects.get(id=ustoz_id)
    fan.delete()
    return redirect('admin_site')

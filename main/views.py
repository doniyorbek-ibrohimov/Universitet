from django.shortcuts import render,redirect
from django.template.context_processors import request

from main.models import *

from re import search

def fan_view(request):
    if request.method=="POST":
        Fan.objects.create(
            nom=request.POST.get('nom'),
            asosiy=request.POST.get('asosiy') if request.POST.get('asosiy') else None,
            yonalish=Yonalish.objects.get(id=request.POST.get('yonalish'))
        )
        return redirect('fanlar')
    search_query = request.GET.get('search', '')
    if search_query:
        fanlar = Fan.objects.filter(nom__icontains=search_query)
    else:
        fanlar = Fan.objects.all()
    context = {
        'fanlar': fanlar,
        'search_param': search_query,
        'yonalishlar':Yonalish.objects.all()
    }
    return render(request, 'fanlar.html', context)

def fan_delete(request,fan_id):
    fan=Fan.objects.get(id=fan_id)
    fan.delete()
    return redirect('admin_site')



def yonalish_delete(request,yonalish_id):
    fan=Yonalish.objects.get(id=yonalish_id)
    fan.delete()
    return redirect('admin_site')

def yonalishlar_view(request):
    if request.method=="POST":
        Yonalish.objects.create(
            nom=request.POST.get('nom'),
            aktiv=request.POST.get('aktiv'),
        )
        return redirect('yonalishlar')
    yonalishlar=Yonalish.objects.all()
    context={
        'yonalishlar':'yonalishlar'
    }
    return render(request,'yonalishlar.html',context)

def ustoz_view(request):
    if request.method=="POST":
        Fan.objects.create(
            ism=request.POST.get('ism'),
            yosh=request.POST.get('yosh') if request.POST.get('asosiy') else None,
            jins=request.POST.get('jins'),
            daraja=request.POST.get('daraja'),
            fan=Fan.objects.get(id=request.POST.get('fan'))
        )
        return redirect('fanlar')
    search_query = request.GET.get('search', '')
    if search_query:
        ustozlar = Ustoz.objects.filter(ism__icontains=search_query)
    else:
        ustozlar = Ustoz.objects.all()
    context = {
        'ustozlar': ustozlar,
        'search_param': search_query
    }
    return render(request, 'ustozlar.html', context)

def ustoz_delete(request,ustoz_id):
    fan=Ustoz.objects.get(id=ustoz_id)
    fan.delete()
    return redirect('admin_site')

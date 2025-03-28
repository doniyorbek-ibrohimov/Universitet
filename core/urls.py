
from django.contrib import admin
from django.urls import path

from main.views import fan_delete, yonalish_delete, ustoz_delete, fan_view, ustoz_view, yonalishlar_view

urlpatterns = [
    path('admin/', admin.site.urls,name='admin-site'),
    path('fan/delete/<int:fan_id>/',fan_delete),
    path('fanlar/',fan_view,name="fanlar"),
    path('yonalish/delete/<int:yonalish_id>/',yonalish_delete),
    path('yonalishlar/',yonalishlar_view,name='yonalishlar'),
    path('ustoz/delete/<int:ustoz_id>/',ustoz_delete),
    path('',ustoz_view)
]

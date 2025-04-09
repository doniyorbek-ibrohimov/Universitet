from tkinter.font import names

from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls,name='admin-site'),
    path('fan/delete/<int:fan_id>/',fan_delete),
    path('fan/delete/<int:pk>/update',fan_update),
    path('fanlar/',fan_view,name="fanlar"),
    path('yonalish/delete/<int:yonalish_id>/',yonalish_delete),
    path('yonalish/<int:pk>/update/',yonalish_update,name="yonalishlar"),
    path('yonalishlar/',yonalishlar_view,name='yonalishlar'),
    path('ustoz/delete/<int:ustoz_id>/',ustoz_delete),
    path('ustoz/<int:ustoz_id>/update/',ustoz_update),
    path('',ustoz_view,name="ustozlar")
]

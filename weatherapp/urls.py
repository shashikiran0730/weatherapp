from django.urls import path
from .import views
from django.http import HttpResponse

urlpatterns=[
    path('',views.index,name='indexs'),
    path('contact',views.contact,name='contactweb'),
]
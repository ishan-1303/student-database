from django.contrib import admin
from django.urls import path
from django.urls import re_path
from stud_info import views

urlpatterns = [
    re_path(r'^studentsapi$',views.Get_students_List.as_view()),
    re_path(r'^home$',views.homepage, name='home'),
    re_path(r'^insert$',views.insertpage, name='insert'),
    re_path(r'^delete$',views.deletepage, name='delete'),
    re_path(r'^update$',views.updatepage, name='update')
]
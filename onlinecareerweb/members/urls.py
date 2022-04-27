from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('aptitude',views.aptitude,name = 'aptitude'),
    path('aptitude_cse',views.aptitude_cse,name = 'aptitude_cse'),
    path('myform',views.myform,name = 'myform'),
    path('aptitude_extc',views.aptitude_extc,name = 'aptitude_extc'),
    path('careeroptions',views.careeroptions,name ='careeroptions'),
    path('login',views.contact,name = 'login'),
    path('register',views.contact,name = 'register'),
    path('contact',views.contact,name = 'contact'),
    path('submitmyform',views.contact,name = 'submitmyform'),
]

from django.urls import path
from myApp import views

urlpatterns=[
    path('',views.home,name='my_home'),
    path('about/',views.about, name='my_about'),
    path('contact/',views.contact, name='my_contacts'),
    path('blog/',views.blog, name='my_blog'),
    path('services/',views.services, name='my_services'),
    path('careers', views.career, name='my_careers'),
]
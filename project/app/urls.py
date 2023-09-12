from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login', views.login, name='login'),
    path('admin', views.admin, name='admin'),
    path('write', views.write, name='write'),
    path('post', views.post, name='post'),   
]
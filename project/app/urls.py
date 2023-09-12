from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'User', views.UserViewSet)
router.register(r'Post', views.PostViewSet)

urlpatterns = [
    path('',views.index, name='index'),
    path('login', views.login, name='login'),
    path('admin', views.admin, name='admin'),
    path('write', views.write, name='write'),
    path('post', views.post, name='post'),
    path('api', include(router.urls)),
]
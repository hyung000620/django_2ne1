from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'User', views.UserViewSet)
router.register(r'Post', views.PostViewSet)

urlpatterns = [
    path('client_board/', views.client_board, name='client_board'),
    path('login/', views.login_page, name='login'),
    path('admin_board/', views.admin_board, name='admin_board'),
    path('board/', views.board, name='board'),
    path('write/', views.write, name='write'),
    path('api', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from ckeditor_uploader import views as ckeditor_uploader_views
from . import views

router = DefaultRouter()
router.register(r'User', views.UserViewSet)
router.register(r'Post', views.PostViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', views.admin, name='admin'),
    path('write/', views.write_post, name='write'),
    path('post/', views.post, name='post'),
    path('api/', include(router.urls)),
    path('signup/', views.signup, name='signup'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
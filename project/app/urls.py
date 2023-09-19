from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import image_upload


app_name = 'app'
urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.post_list, name='post_list'),
    path('post_list/<str:topic>/', views.post_list, name='post_list_by_topic'),
    path('api/blog_posts/', views.BlogPostList.as_view(), name='blogpost-list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('write/', views.create_or_update_post, name='create_or_update_post'),
    path('edit_post/<int:post_id>/', views.create_or_update_post, name='create_or_update_post'),
    path('image-upload/', image_upload.as_view(), name='image_upload'),
    path('image_crawl/', views.img_crawling, name='image_crawl'),
    path('execute_selenium/', views.execute_selenium, name="execute_selenium"),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('execute_chatbot/', views.execute_chatbot, name='execute_chatbot'),
]
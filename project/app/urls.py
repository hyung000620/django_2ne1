from django.urls import path
from . import views

urlpatterns = [
    path('client_board/', views.client_board, name='client_board'),
    path('login/', views.login_page, name='login'),
    path('admin_board/', views.admin_board, name='admin_board'),
    path('board/', views.board, name='board'),
    path('write/', views.write, name='write'),
]
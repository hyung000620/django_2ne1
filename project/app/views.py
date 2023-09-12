from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import User, Post
from .serializers import UserSerializer, PostSerializer
import random
# Create your views here.
def index(request):
    return render(request, 'index.html')


def board(request):
    return render(request, 'board.html')

def login_page(request):
    return render(request, 'login.html')

def board_client(request):
    return render(request, 'board_client.html')

def client_board(request):
    return render(request, 'client_board.html')

def board_admin(request):
    return render(request, 'board_admin.html')

def admin_board(request):
    return render(request, 'admin_board.html')

def write(request):
    return render(request, 'write.html')

def post(request):
    return render(request, 'post.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
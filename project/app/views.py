from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import User, Post
from .serializers import UserSerializer, PostSerializer
import random
# Create your views here.
def index(request):
    is_logined = False
    return render(request, 'index.html',{"is_logined":is_logined})
def admin(request):
    is_logined = True
    return render(request, 'index.html', {"is_logined":is_logined})

def login(request):
    return render(request, 'user/login.html')

def write(request):
    return render(request, 'post/write.html')

def post(request):
    return render(request, 'post/post.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

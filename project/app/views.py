from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .forms import PostForm
from .models import User, Post
from .serializers import UserSerializer, PostSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db import IntegrityError
from django.db.models import Q
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

# 회원가입
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        try:
            if form.is_valid():
                user = form.save()
                login(request, user)  # 회원가입 후 자동 로그인
                return redirect('index')  # 가입 후 홈 페이지로 리다이렉트
        except IntegrityError as e:
            error_message = "이미 사용 중인 이메일 주소 또는 아이디입니다."
            return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message})
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# 포스트 검색
def search_posts(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        results = Post.objects.all()
    return render(request, 'post/search_posts.html', {'results': results})

# 글 작성
def write_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'post/write.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/post_detail.html', {'post': post})

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'post/edit_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')  # 이동할 URL을 수정해야 할 수 있습니다.
    
    return render(request, 'post/delete_post.html', {'post': post})
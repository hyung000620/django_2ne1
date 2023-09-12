from django.shortcuts import render

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
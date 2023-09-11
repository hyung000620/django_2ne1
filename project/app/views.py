from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

#test
def board(request):
    return render(request, 'board.html')

def login_page(request):
    return render(request, 'login.html')

def client_board(request):
    return render(request, 'client_board.html')

def admin_board(request):
    return render(request, 'admin_board.html')

def write(request):
    return render(request, 'write.html')
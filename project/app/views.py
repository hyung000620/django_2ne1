from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import View
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import default_storage

from rest_framework import generics
from bs4 import BeautifulSoup

from .serializers import BlogPostSerializer
from .forms import CustomLoginForm, BlogPostForm

from .models import BlogPost

import openai  # GPT-3 라이브러리

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('app:post_list')
    
    else:
        form = CustomLoginForm(data=request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('app:post_list')
        return render(request, 'registration/login.html', {'form': form})

def post_list(request, topic=None):
    if topic:
        posts = BlogPost.objects.filter(topic=topic, publish='Y').order_by('-views')
    
    else:
        posts = BlogPost.objects.filter(publish='Y').order_by('-views') 
    return render(request, 'app/post_list.html', {'posts': posts})

class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

def create_or_update_post(request, post_id=None):
    if post_id:
        post = get_object_or_404(BlogPost, id=post_id)
    
    else:
        post = BlogPost.objects.filter(author_id=request.user.username, publish='N').order_by('-created_at').first()

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)

            if 'delete-button' in request.POST:
                post.delete() 
                return redirect('app:post_list') 

            if not form.cleaned_data.get('topic'):
                post.topic = '전체'
            
            if 'temp-save-button' in request.POST:
                post.publish = 'N'
            else:
                post.publish = 'Y'

            post.author_id = request.user.username

            post.save()
            return redirect('app:post_detail', post_id=post.id)
    
    else:
        form = BlogPostForm(instance=post)

    template = 'app/write.html'
    context = {'form': form, 'post': post, 'edit_mode': post_id is not None, 'MEDIA_URL': settings.MEDIA_URL,} #edit_mode: 글 수정 모드여부

    return render(request, template, context)




def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST': 
        if 'delete-button' in request.POST:
            post.delete()
            return redirect('app:post_list')

    post.views += 1 
    post.save() 

    previous_post = BlogPost.objects.filter(id__lt=post.id, publish='Y').order_by('-id').first()
    next_post = BlogPost.objects.filter(id__gt=post.id, publish='Y').order_by('id').first()

    recommended_posts = BlogPost.objects.filter(topic=post.topic, publish='Y').exclude(id=post.id).order_by('-created_at')[:2]
    for recommended_post in recommended_posts:
        soup = BeautifulSoup(recommended_post.content, 'html.parser')
        image_tag = soup.find('img')
        recommended_post.image_tag = str(image_tag) if image_tag else ''
    
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
        'recommended_posts': recommended_posts,
        'MEDIA_URL': settings.MEDIA_URL,
    }

    return render(request, 'app/post.html', context)

class image_upload(View):
    def post(self, request):
        file = request.FILES['file']
        filepath = 'uploads/' + file.name
        filename = default_storage.save(filepath, file)
        file_url = settings.MEDIA_URL + filename
        return JsonResponse({'location': file_url})



openai.api_key = ''

def autocomplete(request):
    if request.method == "POST":
        prompt = request.POST.get('title')
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
            )
            message = response['choices'][0]['message']['content']
        except Exception as e:
            message = str(e)
        return JsonResponse({"message": message})
    return render(request, 'autocomplete.html')


def execute_selenium(request):

    driver = webdriver.Chrome()
    try:
        driver.execute_script("window.open('http://127.0.0.1:8000/login');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        username_input = driver.find_element(By.ID, 'id_username')
        username_input.send_keys("admin")
        userpw_input = driver.find_element(By.ID, 'id_password')
        userpw_input.send_keys("1234")
        username_input.send_keys(Keys.RETURN)

        just_write_button = driver.find_element(By.CLASS_NAME, 'primary-button')
        just_write_button.click()
        
        title = driver.find_element(By.ID, 'title')
        title.send_keys("test")
        autocomplete_button = driver.find_element(By.ID, 'aiAutocompleteButton')
        autocomplete_button.click()
        time.sleep(30)
    finally:
        driver.quit()
    return render(request, 'app/post_list.html')

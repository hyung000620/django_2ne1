from django.db import models

# Create your models here.
class User(models.Model):
    user_id     = models.CharField(verbose_name="사용자 ID", max_length=30)
    name        = models.CharField(verbose_name="사용자 이름", max_length=30)
    password    = models.CharField(verbose_name="사용자 비밀번호", max_length=150)
    
    
class Post(models.Model):
    title       = models.CharField(verbose_name="제목", max_length=30)
    content     = models.TextField(verbose_name="내용")
    tag         = models.CharField(verbose_name="태그", max_length=30)
    created_at  = models.DateTimeField(verbose_name="작성일", auto_now= True)
    img         = models.ImageField(verbose_name="이미지 파일")
    user        = models.ForeignKey(User, on_delete=models.CASCADE)

    
    
    
    
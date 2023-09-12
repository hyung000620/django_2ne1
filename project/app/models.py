from django.db import models

# Create your models here.
class User(models.Model):
    userid    = models.CharField(verbose_name="아이디", max_length=50)
    username    = models.CharField(verbose_name="이름", max_length=50)
    email       = models.EmailField(verbose_name="이메일",default='example@example.com', unique=True)
    password    = models.CharField(verbose_name="비밀번호", max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title       = models.CharField(verbose_name="제목", max_length=200)
    content     = models.TextField(verbose_name="내용")
    tag         = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name="태그", max_length=50)
    created_at  = models.DateTimeField(verbose_name="작성일", auto_now= True)
    updated_at  = models.DateTimeField(verbose_name="수정일",blank=True, null=True)
    img         = models.ImageField(verbose_name="이미지 파일")
    user        = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    name        = models.CharField(verbose_name="카테고리 명칭",max_length=100)
    description = models.TextField(verbose_name="카테고리 설명",blank=True, null=True)
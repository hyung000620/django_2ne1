from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# 사용자 모델
class User(models.Model):
    userid = models.CharField(verbose_name="아이디", max_length=50)
    username = models.CharField(verbose_name="이름", max_length=50)
    email = models.EmailField(verbose_name="이메일", unique=True)
    password = models.CharField(verbose_name="비밀번호", max_length=100)
    date_joined = models.DateTimeField(verbose_name="가입일", auto_now_add=True)

    def __str__(self):
        return self.username

# 태그 모델
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# 포스트 모델
class Post(models.Model):
    title = models.CharField(verbose_name="제목", max_length=200)
    content = models.RichTextField(verbose_name="내용")
    tags = models.ManyToManyField(Tag, verbose_name="태그")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now=True)
    updated_at = models.DateTimeField(verbose_name="수정일", blank=True, null=True)
    img = models.ImageField(verbose_name="이미지 파일", upload_to="post_images")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    topic = models.CharField(verbose_name="주제", max_length=100, default=timezone.now)
    views = models.IntegerField(verbose_name="조회수", default=0)

    def __str__(self):
        return self.title

# 카테고리 모델
class Category(models.Model):
    name = models.CharField(verbose_name="카테고리 명칭", max_length=100)
    description = models.TextField(verbose_name="카테고리 설명", blank=True, null=True)

    def __str__(self):
        return self.name

# 자동완성
class AutocompleteModel(models.Model):
    keyword = models.CharField(max_length=255, unique=True)
    suggestions = models.TextField()  # 자동 완성 제안을 저장할 필드

    def __str__(self):
        return self.keyword
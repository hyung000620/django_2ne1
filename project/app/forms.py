from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'img'] # tag 모델부분에 정의가 안되어있어서 뺏습니다.
    
    widgets = {
        'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요'}),
        'content': forms.Textarea(attrs={'placeholder': '내용을 입력하세요'}),
    }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 1:
            raise forms.ValidationError("제목은 최소 1자 이상이어야 합니다.")
        return title
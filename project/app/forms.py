from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'img']

    widgets = {
        'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요'}),
        'content': CKEditorUploadingWidget(),
    }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 1:
            raise forms.ValidationError("제목은 최소 1자 이상이어야 합니다.")
        return title

    # img 필드는 이미지 업로드를 위한 필드입니다.

    # MyForm에서 사용할 필드들을 PostForm으로 복사
    title = forms.CharField(required=True)
    content = forms.CharField(widget=CKEditorWidget())
    tag = forms.CharField(required=True)
    img = forms.ImageField(required=True)  # img 필드 추가

    # PostForm에서 사용한 Meta 클래스와 fields를 재사용
    class Meta:
        model = Post
        fields = ('title', 'content', 'tag', 'img')
    
    # 자동완성
class AutocompleteForm(forms.Form):
    query = forms.CharField(label='검색어', max_length=100)
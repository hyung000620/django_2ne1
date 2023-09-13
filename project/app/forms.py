from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tag', 'img']

    widgets = {
        'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요'}),
        'content': CKEditorUploadingWidget(),
    }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 1:
            raise forms.ValidationError("제목은 최소 1자 이상이어야 합니다.")
        return title

    def save(self, commit=True):
        instance = super().save(commit=False)
        # 여기에 추가할거 있으면 작업
        if commit:
            instance.save()
        return instance
    
    # 자동완성
class AutocompleteForm(forms.Form):
    query = forms.CharField(label='검색어', max_length=100)
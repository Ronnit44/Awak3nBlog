from django import forms
from .models import Comment,Post
from django.utils import timezone

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
class PostAdminForm(forms.ModelForm):
    created_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), input_formats=['%Y-%m-%dT%H:%M'])

    class Meta:
        model = Post
        fields = '__all__'
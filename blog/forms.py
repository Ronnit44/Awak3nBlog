from django import forms
from .models import Comment,Post
from django.utils import timezone

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
<<<<<<< HEAD
=======

>>>>>>> 5a4eed5039ef24126696f1c0d815e0ccfe89f614
class PostAdminForm(forms.ModelForm):
    created_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), input_formats=['%Y-%m-%dT%H:%M'])

    class Meta:
        model = Post
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = '__all__'
>>>>>>> 5a4eed5039ef24126696f1c0d815e0ccfe89f614

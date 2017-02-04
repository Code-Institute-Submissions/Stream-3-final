from django import forms
from .models import Subject, Thread, Post

class ThreadForm(forms.ModelForm):
    name =forms.CharField(label='Thread Name', widget=forms.TextInput(attrs={'placeholder': 'What is your discussion about?'}))
    is_a_poll = forms.BooleanField(label="Include a Poll?", required=False)
    class Meta:
        model = Thread
        fields = ['name']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['comment']
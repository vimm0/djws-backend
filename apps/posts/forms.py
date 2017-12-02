from django import forms

# from pagedown.widgets import PagedownWidget
from froala_editor.widgets import FroalaEditor

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=FroalaEditor())
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]

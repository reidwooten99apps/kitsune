from django import forms

from .models import Post


class ReplyForm(forms.ModelForm):
    """Reply form for forum threads."""
    content = forms.CharField(
                min_length=5,
                max_length=10000,
                widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))

    class Meta:
        model = Post
        exclude = ('thread', 'author')


class NewThreadForm(forms.Form):
    """Form to start a new thread."""
    title = forms.CharField(min_length=5, max_length=255,
                            widget=forms.TextInput(attrs={'size': 80}))
    content = forms.CharField(
                min_length=5,
                max_length=10000,
                widget=forms.Textarea(attrs={'rows': 30, 'cols': 76}))

from django import forms
from users.models import User
from posts.models import Post, Comment


class UserFilterForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='All posts')


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'user_id']


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'user_id']

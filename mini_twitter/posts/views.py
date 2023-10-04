from django.shortcuts import render
from posts.models import Post, Comment
from .forms import UserFilterForm


def index(request):
    posts_list = Post.objects.all()
    title = 'All posts'
    selected_user = None

    if request.method == 'POST':
        form = UserFilterForm(request.POST)
        if form.is_valid():
            selected_user = form.cleaned_data['user']
            title = f"Posts by {selected_user.username if selected_user else 'All Users'}"
            if selected_user:
                posts_list = Post.objects.filter(user=selected_user)
    else:
        form = UserFilterForm()

    context = {'posts': posts_list, 'title': title, 'form': form, 'selected_user': selected_user}
    return render(request, 'posts/posts_list.html', context)


def comment_view(request):
    comments_list = Comment.objects.all()
    context = {'comments': comments_list, 'title': 'All comments'}
    return render(request, 'posts/comments_list.html', context)


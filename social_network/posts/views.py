from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comment
from posts.forms import UserFilterForm, AddPost, AddComment


def posts_view(request):
    posts_list = Post.objects.all()
    title = 'All posts'
    selected_user = None

    if request.method == 'POST':
        form = UserFilterForm(request.POST)

        if form.is_valid():
            selected_user = form.cleaned_data['user']
            title = f'Posts by {selected_user}'
            posts_list = Post.objects.filter(user_id=selected_user)
    else:
        form = UserFilterForm()

    context = {'posts': posts_list, 'title': title, 'form': form, 'selected user': selected_user}
    return render(request, "posts/posts_list.html", context=context)


def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid:
            form.save()
            return redirect('all_posts')
    else:
        form = AddPost()
    return render(request,"posts/add_post.html", {'form': form})


def comment_view(request, selected_post):
    comments = Comment.objects.filter(post_id=selected_post)
    post = Post.objects.get(id=selected_post)
    context = {'comments': comments, 'post': post}
    return render(request, "posts/comments_list.html", context=context)


def add_comment(request, selected_post):
    post = get_object_or_404(Post, pk=selected_post)

    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post
            comment.save()
            return redirect('comments', selected_post=selected_post)
    else:
        form = AddComment()

    context = {'form': form, 'selected_post': selected_post}
    return render(request, "posts/add_comment.html", context)


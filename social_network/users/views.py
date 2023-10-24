from django.shortcuts import render, get_object_or_404
from users.models import User
from posts.models import Post


def users_view(request):
    user_list = User.objects.all()
    context = {'title': 'All users', 'users': user_list}
    return render(request, "users/users_list.html", context=context)


def user_info(request, selected_user):
    profile = get_object_or_404(User, pk=selected_user)
    title = f"{profile}'s profile"
    context = {'title': title, 'profile': profile}
    return render(request, "users/users_info.html", context=context)


def posts_by_user(request, selected_user):
    posts = Post.objects.filter(user_id=selected_user)
    title = f"{get_object_or_404(User, pk=selected_user)}'s posts"
    context = {'title': title, 'posts': posts}
    return render(request, "users/posts_by_user.html", context=context)

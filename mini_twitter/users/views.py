from django.shortcuts import render
from users.models import User


def index(request):
    users_list = User.objects.all()
    context = {'users': users_list, 'title': 'All users'}
    return render(request, 'users/users_list.html', context)

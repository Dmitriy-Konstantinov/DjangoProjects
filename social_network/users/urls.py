from django.urls import path
from .views import users_view, user_info, posts_by_user


urlpatterns = [
    path('', users_view, name='all_users'),
    path('<int:selected_user>/', user_info, name='user_info'),
    path('userposts/<int:selected_user>/', posts_by_user, name='posts_by_user')
]

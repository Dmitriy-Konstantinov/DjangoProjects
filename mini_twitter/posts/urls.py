from django.urls import path
from .views import index, comment_view


urlpatterns = [
    path('', index, name='all_posts'),
    path('comments/', comment_view, name='comment_view')
]

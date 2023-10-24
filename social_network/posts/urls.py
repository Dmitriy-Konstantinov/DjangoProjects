from django.urls import path
from .views import posts_view, add_post, add_comment, comment_view


urlpatterns = [
    path('', posts_view, name='all_posts'),
    path('new_post/', add_post, name='new_post'),
    path('new_comment/<int:selected_post>/', add_comment, name='new_comment'),
    path('comment_view/<int:selected_post>', comment_view, name='comments')
]

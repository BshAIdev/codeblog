
from django.urls import path, include
from main.views import index, blog, posting,new_post

urlpatterns = [
    path('', index,name='index'),
    path('board/', blog,name='blog'),
    path('board/view/<int:pk>',posting, name="posting"),
    path('board/new_post/', new_post, name="new_post"),
]
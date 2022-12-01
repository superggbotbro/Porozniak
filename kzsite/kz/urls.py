
from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('', index,name='home'),
    path('about/', about, name='about'),
    path('contact/', contact,name='contact'),
    path('Review/', review, name='review'),
    path('tour/',tour,name='tour'),
    path('post/<int:post_id>/',show_post,name='post'),
    path('category/<int:cat_id>/',show_category,name='category')


]


from django.urls import path,re_path
from blog.views import index
from blog.views import post_details
from blog.views import category_buttons

urlpatterns = [
    path('', index,name='index'),
    path('<int:id>', post_details),
    path('/', category_buttons, name='category_buttons'),
]


from django.urls import path,re_path
from blog.views import index
from blog.views import post_details

urlpatterns = [
    path('', index,name='index'),
    path('<int:id>', post_details),
]

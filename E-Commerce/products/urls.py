from django.urls import path,re_path
from products.views import index, display, category_buttons, details_page

urlpatterns = [
    path('', display,name='display'),
    path('products', index, name='index' ),
    path('filter/<int:id>', category_buttons, name='category_buttons'),
    path('<int:id>', details_page, name='details_page'),
]

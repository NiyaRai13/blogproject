from django.urls import path
from .views.auth_views import login,register,logout_page
from .views.main_views import index,addblog,blog_page,edit_blog

urlpatterns=[
    path('login/',login, name='login'),
    path('logout/',logout_page,name='logout_page'),
    path('register/', register, name='register'),
    path('addblog/',addblog,name='addblog'),
    path('', index, name='index'),
    path('blog/<int:id>', blog_page, name='blog_page'),
    path('editblog/<int:id>', edit_blog, name='edit_blog'),
]
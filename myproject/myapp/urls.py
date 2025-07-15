from django.urls import path
from .views.auth_views import login,register,logout_page
from .views.main_views import index,addblog,blog_page,edit_blog,delete_blog,profile,change_password

urlpatterns=[
    path('login/',login, name='login'),
    path('logout/',logout_page,name='logout_page'),
    path('register/', register, name='register'),
    path('addblog/',addblog,name='addblog'),
    path('', index, name='index'),
    path('blog/<int:id>', blog_page, name='blog_page'),
    path('editblog/<int:id>', edit_blog, name='edit_blog'),
    path('deleteblog/<int:id>', delete_blog, name='delete_blog'),
    path('profile/<int:id>', profile, name='profile'),
    path('change_password/<int:id>', change_password, name='change_password'),
]
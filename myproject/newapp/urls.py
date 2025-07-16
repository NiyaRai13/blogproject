from django.urls import path
from newapp.views.main_views import index

urlpatterns=[
    path('index/',index,name='index'),
]
from django.urls import path
from .views import index
from .views import register
from.views import login


from . import views
urlpatterns=[
     path('register',views.register,name='register'),

    path('',views.index,name='index'),
    path('login', views.login, name='login'),
  
]
     
    
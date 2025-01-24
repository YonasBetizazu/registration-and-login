from django.urls import path,include
from . import views
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.my_login, name='my-login'),
    path('logout', views.user_logout, name='user_logout'),
    path('home', views.homepage, name='home'),

]
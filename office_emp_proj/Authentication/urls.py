from django.contrib import admin
from django.urls import include,path
from django.contrib.auth import views as authentication_views
from .views import user_views,profilepage

from django.conf import settings
from django.conf.urls.static import static

app_name='authentication'
urlpatterns = [
    path('register/',user_views,name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name="login"),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name="logout"),
    path('profile/',profilepage,name="Profile")

] 
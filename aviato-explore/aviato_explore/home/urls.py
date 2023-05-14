from django.urls import path, include
from home import views as home_views
from django.contrib.auth.views import LoginView, LogoutView
 
 
urlpatterns = [
    path("", home_views.assistant, name="assistant-page"),
 
    # login-section
    path("auth/login/", home_views.login, name="login-page"),
    path("auth/sign-up/", home_views.register, name="register")
    # path("auth/logout/", home_views.login, name="login-page"),
]

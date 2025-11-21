from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm


app_name = 'accounts2'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm), name='login'),
    path('logout/', views.CustomLogoutView.as_view(next_page='testapp:index'), name='logout'),
    ]
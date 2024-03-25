from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView

#from .forms import LoginForm

app_name = "quotes"

urlpatterns = [
    # ... інші URL-адреси ...
    path('', views.main, name='main'),  # URL-адреса для головної сторінки
    path('quote/', views.quote, name='quote'),
    path('author/', views.author, name='author'),     
    path('tag/', views.tag, name='tag'),
]
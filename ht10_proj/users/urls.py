from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.RegisterView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('', views.LoginView.as_view(), name='index'), # Додайте цей рядок
]

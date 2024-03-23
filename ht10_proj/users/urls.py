# from django.urls import path
# from . import views

# app_name = "users"

# urlpatterns = [
#     path("signup/", views.RegisterView.as_view(), name="signup"),
#     path('login/', views.LoginView.as_view(), name='login'),
# ]
# users/urls.py
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.RegisterView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('index/', views.index, name='index'),  # Додайте цей рядок
]

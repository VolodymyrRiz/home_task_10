
# from . import views
# from django.urls import path

# app_name = 'quotes'
# urlpatterns = [
#     path('', views.main, name='root')
# ]

# quotes/urls.py
from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    # ... інші URL-адреси ...
    path('', views.main, name='main'),  # URL-адреса для головної сторінки
]
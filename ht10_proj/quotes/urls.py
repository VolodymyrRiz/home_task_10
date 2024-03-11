
from . import views
from django.urls import path

app_name = 'quotes'
urlpatterns = [
    path('', views.main, name='root')
]

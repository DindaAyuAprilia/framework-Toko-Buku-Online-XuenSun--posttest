from django.urls import path
from . import views

urlpatterns = [
path('', views.homepage, name="homepage"),
path('buku/', views.detail_buku, name="detail_buku"),
]
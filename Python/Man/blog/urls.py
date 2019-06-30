from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('contacty/', views.contacty, name='blog-contacty'),

]
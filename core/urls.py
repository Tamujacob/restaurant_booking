from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.admin_login, name='login'),
    path('order/', views.place_order, name='place_order'),
    path('feedback/', views.submit_feedback, name='submit_feedback')
]
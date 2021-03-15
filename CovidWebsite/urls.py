from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('home/symptom/', views.symptoms, name='symptom'),
    path('account/', views.account, name='account'),

]
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
   path('', views.login, name = "login"),
   path('home/', views.home, name = "home"),
   path('register/', views.register, name ="register"),
   path('signout/', views.signout, name="signout"),
   path('patientregistration/', views.patientregistration1, name = "patientregistration1"),
   path('billing/', views.billing, name="billing"),
   path('dashboard/', views.dashboard, name="dashboard"),
   path('delete/<int:pk>', views.delete, name="delete"),
   path('edit/<int:pk>', views.edit, name = "edit"),
   
]



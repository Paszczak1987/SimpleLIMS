from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_view'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]

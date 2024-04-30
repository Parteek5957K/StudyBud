from django.urls import path
from . import views

urlpatterns = [
    path('lobby/', views.lobby, name="lobby"),
    path('room/', views.room),
    path('', views.home, name="home"),
    path('login/', views.loginpage, name="login"),
    path('signup/', views.signuppage, name="signup"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('solo_study/', views.solo_study, name="solo_study"),
    path('group_study/', views.group_study, name="group_study"),
]

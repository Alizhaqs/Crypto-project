from django.urls import path, include
from .views import *
urlpatterns = [
    path('', MainPage,name='main-page'),
    path('indexes', IndexesPage,name='indexes'),

    path('login', loginView, name='login'),
    path('logout', logoutView, name='logout'),
    path('auth-register', RegisterView, name='auth-register'),
]

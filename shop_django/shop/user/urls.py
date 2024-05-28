from shop.urls import path
from user import views

urlpatterns: list [
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
]

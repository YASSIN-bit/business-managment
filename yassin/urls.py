from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name=''),
    path('register', views.register, name='register'),
    path('login', views.login_view, name ='login'),
    # path('', views.user),
    
]

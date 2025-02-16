from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('yassin.urls'))
]

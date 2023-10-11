"""
URL configuration for user_registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('User_login/',User_login,name='User_login'),
    path('change_password/',change_password,name='change_password'),
    path('details_required/',details_required,name='details_required'),
    path('User_logout/',User_logout,name='User_logout'),
    path('forgot_password/',forgot_password,name='forgot_password'),
    path('registration/',registration,name='registration'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

"""challenge_python_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls.conf import include
from api import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#router = routers.DefaultRouter()
#router.register(r'breweries', views.OpenBreweries, basename="breweries")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("breweries/", views.OpenBreweries.as_view(), name="get-custom-match",),
    path("post-challenge/", views.PostChallenge.as_view(), name="post-challenge",),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh", TokenRefreshView.as_view()),
]

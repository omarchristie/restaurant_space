"""restaurant_space URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from accounts import views as accview
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r"^$", views.HomePage.as_view(), name="home"),
    url(r"^accounts/", include("accounts.urls", namespace="accounts")),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^loginpage/$", views.LoginPage.as_view(), name="loginpage"),
    url(r"^thanks/$", views.ThanksPage.as_view(), name="thanks"),
    url(r"^restaurant/",include("restaurant.urls", namespace="restaurant")),
    url(r"^ratings/",include("ratings.urls", namespace="ratings")),
    url(r"^recommendation/",include("recommendation.urls", namespace="recommendation"))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
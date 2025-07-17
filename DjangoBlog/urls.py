"""
URL configuration for DjangoBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
#Kendi view'ı yani site sayfamızı dahil ediyoruz
from article import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name= "admin"),
    path('', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    #Uygulama içinde bir adet url dosyası oluşturduk. Yani bize /articles/create diye bir fonksiyon geldiğinde önce article'ı bulucak daha sonra articles onu create'e götürecek.
    path('articles/', include("article.urls")),
    path('user/', include("user.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
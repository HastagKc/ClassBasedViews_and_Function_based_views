"""
URL configuration for CBVs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', views.myview, name='func'),
    path('class/', views.MyView.as_view(), name='class'),

    # context
    path('homeview/', views.homeview, name='homeview'),
    path('homeclassview/', views.HomeClassView.as_view(), name='homeclassview'),

    # form
    path('func_form/', views.formview, name='formview')
]

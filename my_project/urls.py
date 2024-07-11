"""
URL configuration for my_project project.

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
from django.urls import path, include
from myapp import views as myappview
from app2 import urls
from app3 import views as app3view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic/', myappview.hi, name= "basic"),
    path('hello/', myappview.hello),
    path('', include(urls)),
    path('signup/', app3view.register),
    path('login/', app3view.login2, name= 'login'),
    path('home2/', app3view.home2, name='home2'),
    path('logout/', app3view.logout2, name= 'logout'),
    # path('hello/<name>', myappview.hello, name="")
]

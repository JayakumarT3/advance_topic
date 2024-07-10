
from django.urls import path
from .views import formfunc


urlpatterns = [
    path('register/', formfunc)
]

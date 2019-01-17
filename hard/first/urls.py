

from django.urls import  path

from . import views

urlpatterns = [
    path('',views.tologin,name='tologin'),
    path('login/',views.login,name='login'),
]
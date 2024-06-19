
from django.urls import path
from . import views
urlpatterns = [
    path('', views.showPage, name="showPage"),
    path('loginpage',views.loginpage,name='loginpageurl'),
    path('register',views.registerpage,name='registerurl'),
]
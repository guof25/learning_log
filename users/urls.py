from django.urls import path
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    #login
    path('login/',login,{'template_name':'users/login.html'},name = 'login'),
    #logout
    path('logout/',views.logout_view,name='logout'),
    #register
    path('register/',views.register,name='register'),
]
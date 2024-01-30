from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect


def custom_logout(request):
     logout(request)
     return render(request, 'info/logout.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('info/', include('info.urls')),
    path('api/', include('apis.urls')),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='info/login.html'), name='login'),
     path('accounts/logout/', custom_logout, name='logout'),
]

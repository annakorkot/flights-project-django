from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views as auth_views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('register/',account_views.register, name ='register'),
    path('update_profile/',account_views.update_profile, name ='update_profile'),
    path('flights/',include('flights.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('',account_views.homepage,name='homepage')
]

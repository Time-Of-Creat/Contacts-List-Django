from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='register'),
    path('home/', views.home, name='home'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('create/', views.contact_create, name='contact_create'),
    path('', include('django.contrib.auth.urls')),
]

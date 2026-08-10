from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='register'),
    path('home/', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
]

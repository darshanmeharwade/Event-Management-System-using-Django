
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/<int:id>/', views.register, name='register'),
    path('my-registrations/', views.my_registrations,
         name='my_registrations'),
]

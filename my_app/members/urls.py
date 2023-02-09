from django.urls import path
from . import views import save

#Padrão funcionando verificar settings
urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('save/', save, name='save')
]
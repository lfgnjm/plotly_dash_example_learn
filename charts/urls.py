from django.urls import path
from . import views

urlpatterns = [
    path('dash/', views.dashboard, name='dashboard'),
    path('dash/<path:path>', views.dashboard, name='dashboard'),
]
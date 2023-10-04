from django.urls import path
from . import views

urlpatterns = [
    path('heads_tails/', views.heads_tails, name='heads_tails'),
]

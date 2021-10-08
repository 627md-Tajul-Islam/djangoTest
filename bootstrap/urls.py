from django.urls import path
from . import views

urlpatterns = [
    path('bootstrap/', views.index, name='bla bla' ),
]
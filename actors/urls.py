from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.ActorListeCreateView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-update-destroy-view'),
]

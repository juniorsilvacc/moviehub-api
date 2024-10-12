from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.GenreListCreateView.as_view(), name='genere-create-list'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genere-detail-update-destroy-view'),
]

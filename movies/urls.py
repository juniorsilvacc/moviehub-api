from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListCreateView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroy.as_view(), name='movie-detail-update-destroy-view'),
]
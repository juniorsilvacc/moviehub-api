from django.contrib import admin
from django.urls import path
from genres.views import GenreListCreateView, GenreRetrieveUpdateDestroyView
from actors.views import ActorListeCreateView, ActorRetrieveUpdateDestroyView
from movies.views import MovieListCreateView, MovieRetrieveUpdateDestroy
from reviews.views import ReviewListCreateView, ReviewRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenreListCreateView.as_view(), name='genere-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genere-detail-update-destroy-view'),
    
    path('actors/', ActorListeCreateView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-update-destroy-view'),
    
    path('movies/', MovieListCreateView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroy.as_view(), name='movie-detail-update-destroy-view'),
    
    path('reviews/', ReviewListCreateView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroy.as_view(), name='review-detail-update-destroy-view'),
]


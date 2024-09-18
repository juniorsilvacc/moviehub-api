from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from actors.views import ActorListeCreateView, ActorRetrieveUpdateDestroyView
from movies.views import MovieListCreateView, MovieRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name='genere'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genere-detail-view'),
    
    path('actors/', ActorListeCreateView.as_view(), name='actor'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
    
    path('movies/', MovieListCreateView.as_view(), name='movie'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroy.as_view(), name='movie-detail-view'),
]


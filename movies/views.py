from django.db.models import Count, Avg
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, views, response, status
from movies.models import Movie
from reviews.models import Review
from movies.serializers import MovieSerializer, MovieListDetailSerializer
from app.permissions import GlobalDefaultPermission


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer

    def get_queryset(self):
        queryset = super().get_queryset()  # Usa o queryset padrão
        search = self.request.GET.get('search')  # Busca por 'search?=NeedForSpeed'

        if search:
            queryset = queryset.filter(title__icontains=search)  # Filtra se houver 'search'

        return queryset


class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer


# É o tipo de view mais genérico, da libertdade de escrever seus próprios métodos
class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_starts = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(
            data={
                'total_movies': total_movies,
                'movies_by_genre': movies_by_genre,
                'total_reviews': total_reviews,
                'average_starts': round(average_starts, 1) if average_starts else 0,
            },
            status=status.HTTP_200_OK,
        )

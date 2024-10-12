from django.db.models import Count, Avg
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, views, response, status
from movies.models import Movie
from reviews.models import Review
from movies.serializers import MovieSerializer
from app.permissions import GlobalDefaultPermission


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request):
        movies = Movie.objects.all()
        search = request.GET.get('search')  # search?=NeedForSpeed

        if search:
            movies = Movie.objects.filter(title__icontains=search)

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


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

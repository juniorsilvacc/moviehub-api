from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor


# Serializar Manual
class MovieSerializerManual(serializers.Serializer):
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)
    resume = serializers.CharField()


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return rate
        return None

        # reviews = obj.reviews.all()  # Acessa todas as avaliações associadas ao filme
        # if reviews.exists():
        #     return sum([review.stars for review in reviews]) / reviews.count()  # Calcula a média
        # return 0  # Se não houver avaliações, retorna 0

    # Validações
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não deve maior do que 200 caracteres.')
        return value

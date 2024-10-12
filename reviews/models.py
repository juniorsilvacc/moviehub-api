from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    # Campo 'movie' é uma ForeignKey, criando uma relação de N-para-1 com o modelo Movie
    # Isso significa que várias resenhas podem estar associadas a um único filme
    # O on_delete=models.PROTECT garante que o filme não possa ser deletado se houver resenhas associadas
    # O related_name='reviews' permite acessar todas as resenhas de um filme usando movie.reviews
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    # Campo 'stars' é um IntegerField que armazena a avaliação em estrelas
    # O campo é validado para aceitar somente valores entre 0 e 5
    # MinValueValidator impede que a avaliação seja menor que 0 e retorna uma mensagem de erro personalizada
    # MaxValueValidator impede que a avaliação seja maior que 5 e também retorna uma mensagem de erro personalizada
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas.')
        ]
    )

    # Campo 'comment' é um TextField que armazena comentários adicionais sobre o filme
    # null=True e blank=True indicam que o campo é opcional, ou seja, pode ser deixado vazio
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.movie)

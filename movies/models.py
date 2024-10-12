from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    # Campo 'title' é um CharField que armazena o título do filme, com um limite de 500 caracteres
    title = models.CharField(max_length=500)

    # Campo 'genre' é uma ForeignKey que cria uma relação de N-para-1 com o modelo Genre
    # Cada filme pode ter um gênero, mas um gênero pode estar associado a muitos filmes
    # on_delete=models.PROTECT evita que o gênero seja deletado se houver filmes relacionados a ele
    # related_name='movies' permite acessar todos os filmes relacionados a um gênero (ex.: genre.movies.all())
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')

    # Campo 'release_date' é um DateField que armazena a data de lançamento do filme
    # null=True e blank=True permitem que o campo seja opcional
    release_date = models.DateField(null=True, blank=True)

    # Campo 'actors' é um ManyToManyField, permitindo que um filme tenha vários atores
    # Cada ator pode estar em vários filmes e cada filme pode ter vários atores
    # related_name='movies' permite acessar todos os filmes em que um ator participou (ex.: actor.movies.all())
    actors = models.ManyToManyField(Actor, related_name='movies')

    # Campo 'resume' é um TextField que armazena uma descrição ou resumo do filme
    # null=True e blank=True permitem que o campo seja opcional
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    # Método especial que define como o objeto Genre será representado como string
    # Quando o objeto for chamado (ex: em uma lista de objetos), o nome do gênero será exibido
    def __str__(self):
        return self.name

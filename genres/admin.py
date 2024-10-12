from django.contrib import admin
from genres.models import Genre


# Usa o decorador para registrar o modelo Genre diretamente no admin
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # list_display especifica quais campos serão exibidos na lista de registros de gênero no admin
    list_display = ('id', 'name')
    # search_fields permite adicionar uma barra de pesquisa no admin para buscar gêneros
    # Aqui, os resultados da pesquisa serão baseados no campo 'name'
    search_fields = ['name']

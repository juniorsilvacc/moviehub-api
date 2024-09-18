from rest_framework import serializers
from genres.models import Genre

# Define um serializer para o modelo Review
class GenreSerializer(serializers.ModelSerializer):
    # Meta classe que define a configuração do serializer
    class Meta:
        # Define qual modelo será utilizado no serializer
        model = Genre
        
        # Indica que todos os campos do modelo Review devem ser incluídos no serializer
        fields = '__all__'
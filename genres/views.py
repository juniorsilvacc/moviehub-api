# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from genres.permissions import GenrePermissionClass

class GenreListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    def get(self, request):
        # Buscar todos e ordena os gêneros por nome
        genres = Genre.objects.all()
        
        # Aplicar o filtro de buscar (search) se o GET estiver presente
        search = request.GET.get('search')
        if search:
            genres = Genre.objects.filter(name__icontains=search)
            
        # Serializa os dados
        serializer = GenreSerializer(genres, many=True)
        
        # Retorna a resposta com os dados filtrados
        return Response(serializer.data, status=status.HTTP_200_OK)

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer















# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         data = [{'id': genre.id, 'name': genre.name} for genre in genres]
#         return JsonResponse(data, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = Genre(name=data['name'])
#         new_genre.save()
#         return JsonResponse(
#             {
#                 'id': new_genre.id, 
#                 'name': new_genre.name
#             }, 
#             status = 201)

# @csrf_exempt
# def genre_detail_view(request, id):
#     # genre = Genre.objects.get(id=id)    
#     genre = get_object_or_404(Genre, id=id)
    
#     if request.method == 'GET':
#         data = {'id': genre.id, 'name': genre.name}
#         return JsonResponse(data)
#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse({'id': genre.id, 'name': genre.name})
#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse({'message': 'Genero excluido com sucesso'}, status=204)
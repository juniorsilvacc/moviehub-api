from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer

class ActorListeCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
    def get(self, request):
        actors = Actor.objects.all()
        
        search = request.GET.get('search')
        if search:
            actors = Actor.objects.filter(name__icontains=search)
        
        serializer = ActorSerializer(actors, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

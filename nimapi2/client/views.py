from api.serializers import ClientSerializers,ProjectSerializer
from .models import Client,Project
from rest_framework import generics

# Create your views here.
class Createclient(generics.CreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializers
 
class ClientList(generics.ListAPIView):
    queryset=Client.objects.all()
    
    serializer_class=ClientSerializers

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

class CreateProjects(generics.CreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ProjectSerializer

class ProjectList(generics.ListAPIView):
    queryset=Project.objects.all()
    serializer_class= ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer





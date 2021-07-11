from django.contrib.auth.models import User
from client.models import Client, Project
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class ClientSerializers(serializers.ModelSerializer):
    clientproject = serializers.SlugRelatedField(many=True,slug_field='project_name',queryset=Project.objects.all())
    class Meta:
        model = Client
        fields = ['id','client_name','created_at','created_by','clientproject']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields ='__all__'

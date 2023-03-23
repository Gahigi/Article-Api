from rest_framework import serializers
from .models import *

class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title', 'author', 'email', 'date']
   
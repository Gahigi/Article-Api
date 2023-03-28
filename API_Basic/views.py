from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import status

# Create your views here.

class ViewAllArticle(APIView):
    def get(self, request):
        print("---------------------------------")
        print(self.__dir__())
        
        articles = Article.objects.all()
        serializers_data = articleSerializer(articles, many= True)
        return Response(serializers_data.data, status= status.HTTP_200_OK)
    def post(self, request):
        serializers_data = articleSerializer(data= request.data)
        if serializers_data.is_valid():
            serializers_data.save()
            return Response(serializers_data.data, status= status.HTTP_201_CREATED)
        return Response(serializers_data.errors, status= status.HTTP_400_BAD_REQUEST)
    
class ViewArticle(APIView):
    def get(self, request, id):
        article = Article.objects.get(id = id)
        serializers_data = articleSerializer(article)
        return Response(serializers_data.data, status= status.HTTP_200_OK)
    def put(self, request, id):
        article = Article.objects.get(id = id)
        serializers_data = articleSerializer(article, data = request.data)
        if serializers_data.is_valid():
            serializers_data.save()
            return Response(serializers_data.data, status= status.HTTP_201_CREATED)
        return Response(serializers_data.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        article = Article.objects.get(id = id)
        article.delete()
        return Response({'status:Deleted'})
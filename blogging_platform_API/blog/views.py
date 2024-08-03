from django.shortcuts import render
from django.http import HttpResponse
from  rest_framework.views import APIView
from .models import Article, Tag
from .serializers import ArticleSerializer, TagSerializer
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return HttpResponse("Hello")


class TagView(APIView):

    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ArticleView(APIView):

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializzer = ArticleSerializer(articles, many=True)
        return Response(serializzer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



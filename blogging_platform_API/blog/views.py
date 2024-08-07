from django.shortcuts import render
from django.http import Http404, HttpResponse
from  rest_framework.views import APIView
from .models import Article, Tag
from .serializers import ArticleSerializer, TagSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

class TagDetailView(APIView):
    # permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            raise Http404
        
    def delete(self, request, pk, format=None):
        try:
            tag = self.get_object(pk)
            tag.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
          

class TagView(APIView):
    # permission_classes = [IsAuthenticated]
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


class ArticleDetailView(APIView):
    # permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)



class ArticleView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        articles = Article.objects.all()
        by_tag = request.query_params.get('tags')
        date_created = request.query_params.get('created_at')
        if by_tag:
            articles = articles.filter(tags__name=by_tag)
        if date_created:
            articles = articles.filter(created_at=date_created)
        serializzer = ArticleSerializer(articles, many=True)
        return Response(serializzer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



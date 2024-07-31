from django.shortcuts import render
from django.http import HttpResponse
from  rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return HttpResponse("Hello")

class ArticleView(APIView):

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializzer = ArticleSerializer(articles, many=True)
        return Response(serializzer.data, status=status.HTTP_200_OK)
    



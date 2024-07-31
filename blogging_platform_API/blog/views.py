from django.shortcuts import render
from django.http import HttpResponse
from  rest_framework.views import APIView


def index(request):
    return HttpResponse("Hello")

class ArticleView(request, data)
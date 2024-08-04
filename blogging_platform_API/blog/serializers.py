from rest_framework import serializers
from .models import Article, Tag

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at']

    def get_created_at(self, obj):
        return obj.created_at.strftime('%d-%m-%Y')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]
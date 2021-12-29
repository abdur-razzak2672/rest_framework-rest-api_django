from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.Serializer):
    article_title = serializers.CharField(max_length = 100)
    article_author = serializers.CharField(max_length = 100)
    article_email = serializers.CharField(max_length = 100)
    article_date = serializers.DateTimeField()

    def create(self , validated_data):
        return Article.all.object.create(validated_data)

    def update(self , instance , validated_data):
        instance.article_title = validated_data.get('article_title' ,instance.article_title)
        instance.article_author = validated_data.get('article_author' ,instance.article_author)
        instance.article_email = validated_data.get('article_email' ,instance.article_email)
        instance.article_date = validated_data.get('article_date' ,instance.article_date)    
        instance.save()
        return instance
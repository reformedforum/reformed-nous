from rest_framework import serializers

from .models import Author, Resource, Topic


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id',
                  'name', )


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id',
                  'name',
                  'media_type',
                  'details', )


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id',
                  'name', )

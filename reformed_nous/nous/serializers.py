from rest_framework import serializers

from .models import Author, Resource, Topic


class AuthorSerializer(serializers.ModelSerializer):
    resources = serializers.HyperlinkedRelatedField(
        source='resource_set',
        many=True,
        read_only=True,
        view_name='resource-detail'
    )

    class Meta:
        model = Author
        fields = ('id',
                  'name',
                  'resources', )


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = (
            'id',
            'name',
            'media_type',
            'authors',
            'topics',
            'details',
        )


class TopicSerializer(serializers.ModelSerializer):
    resources = serializers.HyperlinkedRelatedField(
        source='resource_set',
        many=True,
        read_only=True,
        view_name='resource-detail'
    )

    class Meta:
        model = Topic
        fields = ('id',
                  'name',
                  'resources', )

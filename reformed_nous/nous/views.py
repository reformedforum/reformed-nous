from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Author, Resource, Topic
from .permissions import IsOwnerOrReadOnly
from .serializers import AuthorSerializer, ResourceSerializer, TopicSerializer


class AuthorViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    """
    Creates, Updates, and retrives Authors
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class ResourceViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    """
    Creates, Updates, and retrives Resources
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class TopicViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    """
    Creates, Updates, and retrives Topics
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (IsOwnerOrReadOnly, )

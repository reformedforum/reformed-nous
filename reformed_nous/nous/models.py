import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Topic(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Resource(BaseModel):
    BOOK = 'BOOK'
    ARTICLE = 'ARTICLE'
    AUDIO = 'AUDIO'
    VIDEO = 'VIDEO'
    AUDIO_COURSE = 'AUDIO_COURSE'
    VIDEO_COURSE = 'VIDEO_COURSE'
    OTHER = 'OTHER'
    MEDIA_TYPE_CHOICES = (
        (BOOK, 'Book'),
        (ARTICLE, 'Article'),
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
        (AUDIO_COURSE, 'Audio course'),
        (VIDEO_COURSE, 'Video course'),
        (OTHER, 'Other'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    media_type = models.CharField(
        max_length=255, choices=MEDIA_TYPE_CHOICES, default=OTHER
    )
    authors = models.ManyToManyField(Author)
    topics = models.ManyToManyField(Topic)
    details = JSONField(blank=True)

    def __str__(self):
        return self.name

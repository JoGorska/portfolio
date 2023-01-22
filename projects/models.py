from django.db import models
from django_extensions.db.fields import AutoSlugField


class Language(models.Model):
    name = models.CharField(max_length=220, unique=True, blank=False, null=False)
    slug = AutoSlugField(populate_from=['name'], blank=False, null=False, editable=False, unique=True)
    documentation = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=220, unique=True, blank=False, null=False)
    slug = AutoSlugField(populate_from=['name'], blank=False, null=False, editable=False, unique=True)
    deployed = models.URLField(blank=True, null=True)
    repository = models.URLField(blank=True, null=True)
    video_presentation = models.URLField(blank=True, null=True)

    purpose = models.TextField(blank=True, null=True)
    languages = models.ManyToManyField(Language, related_name='project', blank=True)
    co_creators = models.TextField(blank=True, null=True)

    cover_image = models.ImageField(blank=True, null=True)
    showpiece_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

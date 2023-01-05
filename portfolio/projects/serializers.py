from rest_framework import serialisers

from .models import Project


class ProjectSerializer(serialisers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'purpose']
from django.shortcuts import render
from django.http import JsonResponse
from .models import Project
from .serializers import ProjectSerializer


def projects_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return JsonResponse(serializer.data, safe=False)

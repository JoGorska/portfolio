from django.contrib import admin
from .models import Project, Language


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('languages', )
    model = Project


class LanguageAdmin(admin.ModelAdmin):
    model = Language


admin.site.register(Project, ProjectAdmin)
admin.site.register(Language, LanguageAdmin)

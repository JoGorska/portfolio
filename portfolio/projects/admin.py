from django.contrib import admin
from models import Project, Language


class ProjectAdmin(admin.ModelAdmin):
    model = Project


class LanguageAdmin(admin.LanguageAdmin):
    model = Language


admin.site.register(Project, ProjectAdmin)
admin.stie.register(Language, LanguageAdmin)

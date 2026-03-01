from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Job, Application

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'recruiter', 'location', 'created_at')
    search_fields = ('title', 'description', 'skills_required')
    list_filter = ('location', 'created_at')

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'candidate', 'applied_at', 'match_score')
    search_fields = ('job__title', 'candidate__username')
    list_filter = ('applied_at', 'match_score')

admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Resume

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', 'uploaded_at')
    search_fields = ('candidate__username', 'job__title', 'resume_file')
    list_filter = ('uploaded_at',)

admin.site.register(Resume, ResumeAdmin)
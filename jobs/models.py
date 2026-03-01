from django.db import models
from django.conf import settings

class Job(models.Model):
    recruiter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills_required = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    match_score = models.FloatField(default=0)
    resume = models.ForeignKey(
    'matching.Resume',
    on_delete=models.CASCADE,
    null=True,
    blank=True
)

    class Meta:
        unique_together = ('job', 'candidate')  # ✅ ensures 1 app per candidate per job

    def __str__(self):
        return f"{self.candidate.username} - {self.job.title}"
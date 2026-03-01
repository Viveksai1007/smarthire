from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    ROLE_CHOICES = (
        ('candidate', 'Candidate'),
        ('recruiter', 'Recruiter'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_approved = models.BooleanField(default=False)  # Admin approval for recruiters

    def save(self, *args, **kwargs):
        # Auto approve candidates
        if self.role == 'candidate':
            self.is_approved = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
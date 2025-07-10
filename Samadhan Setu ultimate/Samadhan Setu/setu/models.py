from django.db import models
from django.utils import timezone

class Grievance(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    adhar = models.CharField(max_length=12) 
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    message = models.TextField()
    location = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True, null=True)
    submitted_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(
    max_length=20,
     choices=[
            ('Pending', 'Pending'),
            ('In Progress', 'In Progress'),  # ✅ Add this
            ('Resolved', 'Resolved'),
        ],
        default='Pending'
    )


    def __str__(self):
        return f"{self.title} - {self.name}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.subject}"

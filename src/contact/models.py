from django.db import models

# Create your models here.
class Email(models.Model):
    name = models.CharField(max_length=128, blank=False)
    subject = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
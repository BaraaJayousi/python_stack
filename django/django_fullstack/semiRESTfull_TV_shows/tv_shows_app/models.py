from django.db import models

# Create your models here.

class TV_shows(models.Model):
    title= models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    notes = models.TextField()
    release_date= models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
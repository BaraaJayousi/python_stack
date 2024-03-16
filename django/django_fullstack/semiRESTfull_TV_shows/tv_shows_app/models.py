from django.db import models
from datetime import datetime

# Create your models here.

#New tv-shows manager, adds custom validation to model inputs at the back-end

class TV_Shows_Manager(models.Manager):
    def tv_show_validation(self, postData):
        errors ={}
        if len(postData['show_title']) < 2:
            errors['show_title'] = "Title should be at least 2 characters"
        if len(self.filter(title=postData['show_title'])) > 0:
            errors['show_title_duplicate'] = "The title you\'re adding already exists, choose another one"
        if len(postData['network_name']) < 3:
            errors['network_name'] = "Network name should be at least 3 characters"
        if len(postData['show_desc']) < 10 and len(postData['show_desc']) > 0:
            errors['show_desc'] = "Show description should be at least 10 characters if provided"
        if datetime.strptime(postData['release_date'], "%Y-%m-%d").date() > datetime.now().date():
            errors['release_date'] = "release date should be in the past"
        return errors

class TV_shows(models.Model):
    title= models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    notes = models.TextField()
    release_date= models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    # Assign the new manager with validation function to the TV show model
    objects = TV_Shows_Manager()
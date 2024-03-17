from django.db import models
import re

# Create your models here.

class UsersValidation(models.Manager):
    def validate_user(self, user_data):
        messages={}
        email_pattern = re.compile('^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$')
        if len(user_data['f_name']) < 2:
            messages['f_name'] = "First name must be more than 2 characters"
        if len(user_data['l_name']) < 2:
            messages['l_name'] = "Last name must be more than 2 characters"
        if not email_pattern.match(user_data['email']):
            messages['email'] = "please provide a valid email address e.g. example@domain.com"
        if self.filter(email=user_data['email']):
            messages['email_duplicate'] = "This email is already taken"
        if len(user_data['password']) < 8:
            messages['password'] = "Password must be atleast 8 characters long"
        if user_data['password'] != user_data['confirm_pw']:
            messages['confirm_pw'] = "Passwords do not match"
        
        return messages

class Users(models.Model):
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(max_length=60)

    objects = UsersValidation()

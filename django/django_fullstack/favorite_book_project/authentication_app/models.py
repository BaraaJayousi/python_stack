from django.db import models
import bcrypt
import re

# Create your models here.

class UsersMethods(models.Manager):
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
            messages['password'] = "Password must be at least 8 characters long"
        if user_data['password'] != user_data['confirm_pw']:
            messages['confirm_pw'] = "Passwords do not match"
        
        return messages
    
    def hash_user_input(self,pw):
        return  bcrypt.hashpw(pw.encode(), bcrypt.gensalt(12)).decode()
    
    def check_login_pw(self, pw, user) : # Returns a boolean => True if password match and False if it doesn't
        return bcrypt.checkpw(pw.encode(), user.password.encode())


class Users(models.Model):
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    #   one to many rel with messages model 
    #   one to many rel with comments model

    objects = UsersMethods()
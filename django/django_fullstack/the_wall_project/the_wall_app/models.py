from django.db import models
from authentication_app.models import Users
import datetime
from django.utils import timezone

# Create your models here.

class MessagesManager(models.Manager):
    def validate_message_deletion(self, message_id):
        errors ={}
        now = timezone.now()
        message_creation_date = self.get(id = message_id).created_at
        delta_time = now - message_creation_date
        if delta_time.total_seconds()/60 > 30:
            errors['delete_message_window'] = "The deletion windows of this post has passed, you could only edit the message now"
        return errors

class Messages(models.Model):
    user_id = models.ForeignKey(Users, related_name='users_messages', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    objects = MessagesManager()
    #   one to many rel with Comments

class Comments(models.Model):
    message_id = models.ForeignKey(Messages, related_name='messages_comments', on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, related_name='users_comments', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
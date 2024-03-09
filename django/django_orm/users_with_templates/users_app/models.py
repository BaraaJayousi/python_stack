from django.db import models

# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()

    def __repr__(self) -> str:
        return f"Name: {self.first_name} {self.last_name} Age: {self.age} Email Address: {self.email}"
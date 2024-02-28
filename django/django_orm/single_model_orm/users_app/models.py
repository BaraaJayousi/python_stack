from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Email Address: {self.email_address}"
# overriding django ORM naming convention for tables
    # Original name <app_name>_<class_name>
    class Meta:
        db_table = "users"

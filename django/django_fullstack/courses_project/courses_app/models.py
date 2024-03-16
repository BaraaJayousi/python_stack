from django.db import models

# Create your models here.

class CoursesManager(models.Manager):
    def validate_courses(self, courseData):
        errors = {}
        if len(courseData['course_name']) < 6:
            errors['course_name'] = "Course name must be greater than 5 characters"
        if len(courseData['course_desc']) < 16 :
            errors['course_desc'] = "Course description must be greater than 15 characters"
        
        return errors


class Courses(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CoursesManager()
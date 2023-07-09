from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255,null=False, blank=False)
    last_name = models.CharField(max_length=255,null=False, blank=False)
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

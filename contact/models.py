from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    tel = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()

from django.db import models

class Members(models.Model):
  fullname = models.CharField(max_length=255)
  soi = models.CharField(max_length=255)
  email = models.CharField(max_length=255, null=True)
  role = models.CharField(max_length=255, default='Developer')

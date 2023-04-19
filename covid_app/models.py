from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Covid(models.Model):
    country = models.CharField(max_length=255)
    confirmed = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
    date = models.DateTimeField(auto_now_add=False)

 

    def __str__(self):
        return self.country

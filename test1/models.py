from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_preferences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, default='New York') 
    pref_1 = models.CharField(max_length=100, default='')
    pref_2 = models.CharField(max_length=100, default='')
    pref_3 = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.id} {self.location} {self.pref_1}  {self.pref_2} {self.pref_3}"
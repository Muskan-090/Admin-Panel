
# user_profiles/models.py
from django.db import models


import openai
import json

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    about = models.TextField()
    areas_of_interest = models.TextField()
    password = models.TextField()
    display_picture = models.CharField(max_length=255, blank=True)

    

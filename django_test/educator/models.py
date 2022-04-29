
from django.db import models

class Educator(models.Model):
    educator_name =  models.CharField(max_length = 100)
    courses_offer = models.CharField(max_length = 100)
    
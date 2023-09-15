from django.conf import settings
from django.db import models


# Create your models here.

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()






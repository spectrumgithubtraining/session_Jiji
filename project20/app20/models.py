from django.db import models

# Create your models here.
# yourappname/models.py
# yourappname/models.py
# yourappname/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)  # In practice, use a more secure method for storing passwords

    def __str__(self):
        return self.username

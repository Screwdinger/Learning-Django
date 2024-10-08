from django.db import models


# makemigrations: create changes and store them in a file
# migrate: apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name
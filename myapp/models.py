from django.db import models

# Create your models here.

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()

    class Meta:
        db_table = "lab_data"

class Library(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()

    class Meta:
        db_table = "labrary_data"

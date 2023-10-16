from django.db import models


# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)

    # def __str__(self):
    #     return self.name
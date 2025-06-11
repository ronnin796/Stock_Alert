from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    sub_category = models.CharField(max_length=100)
    restock_threshold = models.IntegerField(default=10)

    def __str__(self):
        return self.name

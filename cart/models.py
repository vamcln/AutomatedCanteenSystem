from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    totalcost = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

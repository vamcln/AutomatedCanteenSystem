from django.db import models

class Fooditem(models.Model):
    image = models.ImageField(upload_to='images/')
    desc = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    cost = models.IntegerField()
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.title

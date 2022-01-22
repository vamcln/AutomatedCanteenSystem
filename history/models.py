from django.db import models
from django.contrib.auth.models import User

class History(models.Model):
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    totalcost = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, default="P")
    order_date = models.DateTimeField()
    reserve_time = models.CharField(max_length=255)

    def __str__(self):
        return self.customer.username
    def date_pretty(self):
        return self.order_date.strftime('%b %e %Y')

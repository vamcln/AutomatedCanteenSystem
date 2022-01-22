from django.db import models
from django.contrib.auth.models import User

class Transactions(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    totalcost = models.IntegerField()
    order_date = models.DateTimeField()

    def __str__(self):
        return self.customer.username
    def date_pretty(self):
        return self.order_date.strftime('%b %e %Y')

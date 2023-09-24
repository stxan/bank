from django.db import models
from django.contrib.auth.models import User


class Transfer(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver_username = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def sender_username(self):
        return self.sender.username

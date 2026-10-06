import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class Merchant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return self.name



class User (AbstractUser):
    merchant = models.ForeignKey(
        Merchant,
        on_delete=models.PROTECT,
        related_name="users",
        null=True,
        blank=True,
    )



    def __str__(self):
        return self.name
# Create your models here.

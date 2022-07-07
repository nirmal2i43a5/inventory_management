from django.db import models
from django.urls import reverse
import uuid

class Supplier(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.EmailField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('supplier-list')

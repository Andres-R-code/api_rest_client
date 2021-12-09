from django.db import models
import uuid

from moduls.clients.models import Client
from moduls.products.models import Product

# Create your models here.


class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        blank=False,
        null=False
        )
    company_name = models.CharField(max_length=150, blank=False, null=False)
    nit = models.IntegerField(blank=False, null=False)
    code = models.UUIDField(default=uuid.uuid4, editable=False)
    products = models.ManyToManyField(Product, related_name='bill')
    created = models.DateField(auto_now_add=True, auto_now=False)
    modified = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Bill'
        verbose_name_plural = 'Bills'
        ordering = ['client_id']

    def __str__(self):
        return f'{self.id} {self.code} {self.client_id} {self.nit}'

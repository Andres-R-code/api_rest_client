from django.db import models

# Create your models here.


class Product(models.Model):
    ATTRIBUTES = (
        ('COLB', 'Color Blue'),
        ('COLR', 'Color Red'),
        ('COLY', 'Color Yellow'),
        ('COLW', 'Color white'),
        ('COLB', 'Color black')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    attribute = models.CharField(max_length=5, choices=ATTRIBUTES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True, auto_now=False)
    modified = models.DateField(auto_now=True, auto_now_add=False)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return f'{self.id} {self.name} {self.attribute}  {self.available}'
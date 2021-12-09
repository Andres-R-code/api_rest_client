from django.db import models

# Create your models here.


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.IntegerField(blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    created = models.DateField(auto_now_add=True, auto_now=False)
    modified = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['first_name']

    def __str__(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.document}'

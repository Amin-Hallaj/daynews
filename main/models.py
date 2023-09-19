from __future__ import unicode_literals
from django.db import models


class Main(models.Model):
    name_site=models.CharField(max_length=100)
    name_page=models.CharField(max_length=100)
    about_us=models.TextField(null=True, blank=True)
    instagram=models.CharField(max_length=100)
    telegram=models.CharField(max_length=100)
    whatsapp=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name_site} | {self.pk}"

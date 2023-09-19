from __future__ import unicode_literals
from django.db import models


class Main(models.Model):
    name_site=models.CharField(max_length=100)
    name_page=models.CharField(max_length=100)
    about_us=models.TextField(null=True, blank=True)
    instagram=models.CharField(max_length=100)
    telegram=models.CharField(max_length=100)
    whatsapp=models.CharField(max_length=100)
    copyright=models.CharField(max_length=100)
    number=models.IntegerField()
    icon_name_header=models.TextField(null=True , blank=True)
    icon_url_header=models.TextField(null=True , blank=True)
    icon_name_footer=models.TextField(null=True , blank=True)
    icon_url_footer=models.TextField(null=True , blank=True)
    favicon_name=models.TextField(null=True , blank=True)
    favicon_url=models.TextField(null=True , blank=True)
    seo_text=models.CharField(max_length=500 , null=True , blank=True)
    seo_keywords=models.TextField(null=True , blank=True)

    def __str__(self):
        return f"{self.name_site} | {self.pk}"

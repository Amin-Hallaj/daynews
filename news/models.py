from __future__ import unicode_literals
from django.db import models
import jdatetime
from django.contrib.auth.models import  User , Permission

class News(models.Model):
    writer=models.ForeignKey(User, on_delete=models.CASCADE, related_name="news")
    title=models.CharField(max_length=500)
    news_text=models.TextField()
    news_in_picname = models.TextField(null=True , blank=True)
    news_in_picurl = models.TextField(null=True , blank=True,)
    picname = models.TextField(null=True , blank=True)
    picurl = models.TextField(null=True , blank=True,)
    news_date = models.FloatField()
    news_category=models.ForeignKey("Category",on_delete=models.CASCADE,related_name="news",null=True , blank=True)
    news_subcategory=models.ForeignKey("SubCategory",on_delete=models.CASCADE,related_name="news",null=True , blank=True)
    slider=models.BooleanField(default=False)
    important=models.BooleanField(default=False)


    def __str__(self):
        return f"{self.writer} | {self.title}"

    @property
    def jdate(self):
        return  jdatetime.datetime.fromtimestamp(self.news_date).strftime("%H:%M:%S %Y/%m/%d")


class Category(models.Model):
    name=models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"
    
    
class SubCategory(models.Model):
    name_sub=models.CharField(max_length=500)
    category=models.ForeignKey("Category",on_delete=models.CASCADE,related_name="subcategory")

    def __str__(self):
        return f"{self.name_sub} | {self.category}"
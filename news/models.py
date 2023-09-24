from __future__ import unicode_literals
from django.db import models
import jdatetime
from django.contrib.auth.models import  User , Permission


class News(models.Model):
    writer=models.ForeignKey(User, on_delete=models.CASCADE, related_name="news")
    title=models.CharField(max_length=500)
    news_brief=models.TextField()
    news_text=models.TextField()
    news_in_picname = models.TextField(null=True , blank=True)
    news_in_picurl = models.TextField(null=True , blank=True,)
    picname = models.TextField(null=True , blank=True)
    picurl = models.TextField(null=True , blank=True,)
    news_date = models.FloatField()

    def __str__(self):
        return f"{self.writer} | {self.title}"

    @property
    def jdate(self):
        return  jdatetime.datetime.fromtimestamp(self.news_date).strftime("%H:%M:%S %Y/%m/%d")
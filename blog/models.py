from datetime import datetime

from django.db import models
from markupfield.fields import MarkupField


class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(db_index=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(db_index=True, unique_for_date='date')
    date = models.DateTimeField('date published', auto_now=True, db_index=True)
    body = MarkupField(default_markup_type='html', max_length=600)

    @property
    def date_for_publish(self):
        return datetime.strftime(self.date, '%Y/%m/%d')

    def __str__(self):
        return self.title

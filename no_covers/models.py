from datetime import datetime

from django.db import models
from markupfield import fields

from django.utils.translation import ugettext_lazy as _


class Book(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    author = models.CharField(_('Author'), max_length=100)
    excerpt = models.TextField(_('Excerpt from a book'), max_length=1500)
    url_link = models.URLField()

    def __str__(self):
        return self.title

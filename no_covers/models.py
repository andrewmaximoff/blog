from django.db import models
from django.utils.translation import ugettext_lazy as _


class Book(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    author = models.CharField(_('Author'), max_length=100)
    excerpt = models.TextField(_('Excerpt from a book'))
    resource = models.CharField(_('Resource'), max_length=100)
    url_link = models.URLField()

    def __str__(self):
        return self.title

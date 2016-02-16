from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

@python_2_unicode_compatible
class Saga(models.Model):
    name = models.CharField(max_length=200) #FIXME unique

    def __str__(self):
        return self.name

    def sorted_publications(self):
        return self.publication_set.order_by('pub_date')

    def link(self):
        url = reverse('saga', kwargs={'sa_id': self.id})
        return mark_safe(u"<a href=\"%s\">%s</a>" % (url, escape(self.name)))


class Editor(models.Model):
    name = models.CharField(max_length=200) #FIXME unique

    def __str__(self):
        return self.name

    def sorted_publications(self):
        return self.publication_set.order_by('pub_date')

    def link(self):
        url = reverse('editor', kwargs={'ed_id': self.id})
        return mark_safe(u"<a href=\"%s\">%s</a>" % (url, escape(self.name)))


@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=200) #FIXME unique
    birthday = models.DateField()
    nation = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def sorted_publications(self):
        return self.publication_set.order_by('saga', 'pub_date')

    def link(self):
        url = reverse('author', kwargs={'au_id': self.id})
        return mark_safe(u"<a href=\"%s\">%s</a>" % (url, escape(self.name)))


@python_2_unicode_compatible
class Publication(models.Model):
    isbn = models.BigIntegerField()
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    volume = models.IntegerField(default=1)
    #first_of_saga is a bad idea since you may buy issues
    #in an unordered manner: your first one wouldn't be the real one
    saga = models.ForeignKey(Saga, on_delete=models.CASCADE)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    pages = models.IntegerField()
    genre = models.CharField(max_length=200)
    note = models.FloatField() #percents, FIXME enforce this
    summary = models.TextField()

    def __str__(self):
        return self.title

    def link(self):
        url = reverse('pub', kwargs={'pub_id': self.id})
        return mark_safe(u"<a href=\"%s\">%s</a>" % (url, escape(self.title)))

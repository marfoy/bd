from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Editor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    nation = models.CharField(max_length=50)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Publication(models.Model):
    isbn = models.BigIntegerField()
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    volume = models.IntegerField(default=1)
    saga = models.CharField(max_length=200)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    pages = models.IntegerField()
    genre = models.CharField(max_length=200)
    note = models.FloatField() #percents, FIXME enforce this
    summary = models.TextField()

    def __str__(self):
        return self.title

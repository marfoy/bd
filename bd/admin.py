from django.contrib import admin
from .models import Publication, Editor, Saga, Author
admin.site.register(Publication)
admin.site.register(Saga)
admin.site.register(Editor)
admin.site.register(Author)

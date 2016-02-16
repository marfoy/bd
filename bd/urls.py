from django.conf.urls import url

from . import views

urlpatterns = [
url(r'^authors', views.authors, name='authors'),
url(r'^author/(?P<au_id>[0-9]+)$', views.author, name='author'),
url(r'^editor/(?P<ed_id>[0-9]+)$', views.editor, name='editor'),
url(r'^pubs', views.pubs, name='pubs'),
url(r'^pub/(?P<pub_id>[0-9]+)$', views.pub, name='pub'),
]

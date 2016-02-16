from django.shortcuts import render, get_object_or_404
from .models import Author, Publication, Editor, Saga

#FIXME remove class=hover

def pub(request, pub_id):
    context = {'p': get_object_or_404(Publication, pk=pub_id)}
    return render(request, 'bd/pub.html', context)

def pubs(request):
    context = {'lst': Publication.objects.order_by('saga', 'pub_date')}
    return render(request, 'bd/pubs.html', context)

def author(request, au_id):
    context = {'a': get_object_or_404(Author, pk=au_id)}
    return render(request, 'bd/author.html', context)

def saga(request, sa_id):
    context = {'s': get_object_or_404(Saga, pk=sa_id)}
    return render(request, 'bd/saga.html', context)

def editor(request, ed_id):
    context = {'e': get_object_or_404(Editor, pk=ed_id)}
    return render(request, 'bd/editor.html', context)

def authors(request):
    context = {'lst': Author.objects.order_by('name')[:10]}
    return render(request, 'bd/authors.html', context)

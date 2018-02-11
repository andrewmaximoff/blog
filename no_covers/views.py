from django.shortcuts import render
from django.views import generic
from django.core.cache import cache

from .models import Book


class IndexView(generic.View):
    model = Book
    template_name = 'no_covers/index.html'

    def get(self, request):
        books = self.model.objects.order_by('?')
        if cache.get(request.session.get('queryset_id')):
            books = cache.get(request.session.get('queryset_id'))
        counter = request.session.get('counter', 0)
        if counter+2 > len(books):
            request.session['counter'] = 0
        else:
            request.session['counter'] = counter + 1
        unique_id = request.session.get('queryset_id', id(books))
        request.session['queryset_id'] = unique_id
        cache.set(unique_id, books, 240)
        return render(request, self.template_name, {'book_list': books,
                                                    'counter': counter})

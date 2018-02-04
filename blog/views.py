from django.http import HttpResponse
from django.views import generic

from .models import Post, Categories


class IndexView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return self.model.objects.order_by('-date')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'


class CategoriesView(generic.ListView):
    model = Categories
    template_name = 'blog/categories.html'
    context_object_name = 'categories_list'


class CategoriesDetailView(generic.DetailView):
    model = Categories
    template_name = 'blog/categories_detail.html'

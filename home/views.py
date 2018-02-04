from django.http import HttpResponse
from django.views import generic, defaults
from django.shortcuts import render_to_response
from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = 'home/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return self.model.objects.order_by('-date')


def handler404(request):
    response = render_to_response('home/404.htm')
    response.status_code = 404
    return response

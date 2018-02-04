from django.http import HttpResponse
from django.views import generic
from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = 'home/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return self.model.objects.order_by('-date')

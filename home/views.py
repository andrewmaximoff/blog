from django.http import HttpResponse
from django.views import generic
from django.template import Context, loader
from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = 'home/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return self.model.objects.order_by('-date')


def handler404(request):
    template = loader.get_template('home/404.htm')
    context = Context({
        'message': 'All: %s' % request,
    })

    return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)

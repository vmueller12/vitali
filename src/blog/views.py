from django.shortcuts import render
from django.views import generic
from .models import Entry
# Create your views here.


class BlogIndex(generic.ListView):
    queryset = Entry.objects.published()
    template_name = "blog/index.html"
    paginate_by = 2
    

class BlogDetail(generic.DetailView):
    model = Entry
    template_name = "blog/post.html"
    
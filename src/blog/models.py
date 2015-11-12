from django.db import models
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse
# Create your models here.

from django.conf import settings




class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
        return self.slug


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)



class Entry(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, height_field=None, width_field=None, max_length=100)
    body = MarkdownField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    tags = models.ManyToManyField(Tag)
    
    objects = EntryQuerySet.as_manager()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={"slug": self.slug})
    
        
    
    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        # appearing reverse cronological order
        ordering = ["-created"]
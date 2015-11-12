from django.contrib.syndication.views import Feed
from .models import Entry


class LatestPosts(Feed):
    title = "Vit Blog"
    link = '/feed/'
    description = "Latest Posts of Vit"
    
    def items(self):
        return Entry.objects.published()[:5]

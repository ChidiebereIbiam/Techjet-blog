from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.post_date
    
    def location (self, obj):
        return '/article/%s' % (obj.pk) 
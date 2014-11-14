from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sportslab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sportslab_scraper.views.search', name = 'home'),
    url(r'^do_scrape/$', 'sportslab_scraper.views.do_scrape', name = 'do_scrape'),
)

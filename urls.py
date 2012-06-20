from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/$', 'polls.views.index'),
    url(r'^polls/vote/$', 'polls.views.vote'),
    url(r'^polls/(?P<sid>\d+)/voted/$', 'polls.views.voted'),
    url(r'^polls/results/$', 'polls.views.results'),
    # Examples:
    # url(r'^$', 'csdiv.views.home', name='home'),
    # url(r'^csdiv/', include('csdiv.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

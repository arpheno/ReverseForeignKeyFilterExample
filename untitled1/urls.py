from django.conf.urls import patterns, include, url
from django.contrib import admin
from reversefk.views import ReverseFK

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', ReverseFK.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)

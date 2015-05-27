from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from ajax.views import myFunction
from reversefk.views import ReverseFK

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^rfk/?$', ReverseFK.as_view()),
    url(r'^ajax/?$', TemplateView.as_view(template_name="ajax/base.html")),
    url(r'^myFunction/?$', myFunction),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('billuisin.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^quiz/', include('quiz.urls')),
    # url(r'^register/$', 'register', name='register'),
)

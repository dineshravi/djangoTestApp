from django.conf.urls import patterns, include, url

from django.contrib import admin
from personal_page import views

# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('personal_page.urls')),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^submit/$', include('personal_page.urls')),
    # url(r'^create/$', include('personal_page.urls')),
    # url(r'^admin/', include(admin.site.urls)),


)

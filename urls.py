from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('mysite.aniface.views',
    (r'^$', 'index'),
    (r'^plist/$', 'pr_list'),
    (r'^config/$', 'confug'),
    (r'^anime/(?P<ap_slug>[\w.+\-]{0,100})/$', 'anime'),
    (r'^mark/(?P<ap_slug>[\w.+\-]{0,100})/$', 'mark'),
    (r'^move/(?P<ap_slug>[\w.+\-]{0,100})/$', 'movepl'),
    (r'^remove/$', 'rm_plist'),
    (r'^add_to_list/$', 'add_plist'),
    (r'^play/(?P<ap_slug>[\w.+\-]{0,100})/$', 'play')
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^af_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.ANI_MEDIA_ROOT}),
)

# Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

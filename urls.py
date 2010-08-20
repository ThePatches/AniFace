from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('mysite.aniface.views',
    (r'^$', 'index'),
    (r'^plist/$', 'pr_list'),
    (r'^anime/(?P<ap_slug>[\w.+\-]{0,100})/$', 'anime'),
    (r'^mark/(?P<ap_slug>[\w.+\-]{0,100})/$', 'mark')
    #(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)


# Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

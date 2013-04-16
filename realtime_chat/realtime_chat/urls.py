from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'realtime_chat.views.home', name='home'),
     url(r'^realtime_chat/', include('realtime_chat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
     url(r'^node_api$', 'core.views.node_api', name='node_api'),
     url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/ login.html'}, name='login'),
     url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)

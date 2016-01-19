from django.conf.urls import patterns, include, url
from django.contrib import admin
from images import views as image_views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^1/', include('one_app.urls')),
    url(r'^2/', include('two_app.urls')),
    url(r'^image/$', image_views.image, name='image'),
    url(r'^build/$', image_views.build, name='build')

)


from django.conf.urls import patterns, include, url
from one_app import views
from images import views as image_views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', views.index, name='one'),
   # url(r'^container/$', image_views.container, name='container'),
    url(r'^image/$', image_views.image, name='image'),
)

from django.conf.urls import patterns, include, url
from two_app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', views.index, name='two'),
)

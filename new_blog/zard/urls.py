from django.conf.urls import include, url,patterns
from . import views

from views import ArticlePublishView,ArticlePublishView2

#patterns or error will occur str' object has no attribute 'resolve' django
urlpatterns = patterns('',
    #url(r'^article/(?P<id>\d+)/$','zard.views.content'),
    url(r'^$','zard.views.index'),
    url(r'^login/$','zard.views.login'),
    url(r'^signin/$','zard.views.signin'),
    url(r'^logoff/$','zard.views.logout'),
    url(r'^dropup/$','zard.views.dropup'),
    url(r'^marks/$','zard.views.marks'),
    url(r'^articles/(?P<caption>.+)/$','zard.views.article'),
    url(r'^publish/$',ArticlePublishView.as_view()),
    url(r'^articles/$','zard.views.articles'),
    url(r'^publish2/$',ArticlePublishView2.as_view()),
    #url(r'^articles/(?P<caption>.+)/edit$','zard.views.publish_article'),


)
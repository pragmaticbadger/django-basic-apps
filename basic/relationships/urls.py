from django.conf.urls.defaults import *


urlpatterns = patterns('basic.relationships.views',
    url(r'^following/(?P<user_id>\d+)/$',
        view='following',
        name='relationship_following'
    ),
    url(r'^followers/(?P<user_id>\d+)/$',
        view='followers',
        name='relationship_followers'
    ),
    url(r'^follow/(?P<to_user_id>\d+)/$',
        view='follow',
        name='relationship_follow'
    ),
    url(r'^unfollow/(?P<to_user_id>\d+)/$',
        view='unfollow',
        name='relationship_unfollow'
    ),
    url(r'^block/(?P<user_id>\d+)/$',
        view='block',
        name='relationship_block'
    ),
    url(r'^unblock/(?P<user_id>\d+)/$',
        view='unblock',
        name='relationship_unblock'
    ),
)
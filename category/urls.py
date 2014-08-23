from django.conf.urls import patterns, url

from category import views

urlpatterns = patterns('',
   # ex: /polls/
    url(r'^new/$', views.new, name='new'),
    url(r'^create/$', views.create, name='create'),
    url(r'^all_categories/$', views.all_categories, name='all_categories'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/create/$', views.create_post, name='create_post'),
    url(r'^all_posts/$', views.all_posts, name='all_posts'),
    url(r'^my_posts/$', views.my_posts, name='my_posts'),
    url(r'^search_post/$', views.search_post, name='search_post'),


    

)
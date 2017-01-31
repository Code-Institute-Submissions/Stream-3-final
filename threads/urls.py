from django.conf.urls import url, include
from threads import views as threads_views

urlpatterns = [
    url(r'^forum/$', threads_views.forum, name='forum'),
    url(r'^threads/(?P<subject_id>\d+)/$', threads_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', threads_views.new_thread, name='new_thread'),
    url(r'thread/(?P<thread_id>\d+)/$', threads_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', threads_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', threads_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<post_id>\d+)/$', threads_views.delete_post, name='delete_post'),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', threads_views.thread_vote, name='cast_vote'),
]
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^flatpages/$', views.post_list, name='flatpages'),

]
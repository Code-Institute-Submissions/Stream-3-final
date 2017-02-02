from django.conf.urls import url
import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^cancel_subscription/$', views.cancel_subscription, name='cancel_subscription'),
    url(r'^resetuser', views.reset_user, name='resetuser'),
    url(r'^reset', views.reset, name='reset'),

]
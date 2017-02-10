from django.conf.urls import url
import views

urlpatterns = [

    url(r'^locations/$', views.get_locations, name='locations'),
]
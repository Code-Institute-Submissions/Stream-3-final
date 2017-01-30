from django.conf.urls import url, include
from magazines import views as magazine_views

urlpatterns = [
    url(r'^magazines/$', magazine_views.all_magazines, name='magazines'),
]
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'', include('home.urls')),
    url(r'', include('accounts.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
]

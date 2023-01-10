from django.contrib import admin
from django.urls import path, include, re_path
from django.views import static
from django.conf import settings
from exam import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', static.serve,
         {'document_root': settings.STATIC_ROOT}, name='static'),
    path('', include(urls)),
]

from django.contrib import admin
from django.urls import include, path

from . import settings

urlpatterns = [
    path('', include('homepage.urls', namespace='index')),
    path('about/', include('about.urls', namespace='about')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

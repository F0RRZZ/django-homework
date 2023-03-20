from django.conf.urls.static import static
from django.contrib import admin
import django.contrib.auth.urls
from django.urls import include, path

from homework import settings

urlpatterns = [
    path('', include('homepage.urls', namespace='index')),
    path('about/', include('about.urls', namespace='about')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include(django.contrib.auth.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

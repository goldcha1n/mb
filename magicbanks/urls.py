from django.conf.urls.static import static
from django.contrib import admin

from magicbanks import settings
from django.urls import path, include

from notes.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
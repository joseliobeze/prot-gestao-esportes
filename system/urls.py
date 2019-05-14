from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import paginicial


urlpatterns = [
    path('admin/', admin.site.urls),
    path('aluno/', include('aluno.urls', namespace='aluno')),
    path('', paginicial.Index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
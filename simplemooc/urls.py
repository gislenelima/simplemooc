from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from simplemooc.core import views
from simplemooc.courses import views
from django.conf.urls.static import static
from django.conf import settings


admin.autodiscover()

urlpatterns = [
    path('', include('simplemooc.core.urls')),
    path('cursos/', include('simplemooc.courses.urls',)),
    path('conta/', include('simplemooc.accounts.urls',)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





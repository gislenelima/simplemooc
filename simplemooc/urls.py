from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from simplemooc.core import views
from simplemooc.courses import views
admin.autodiscover()

urlpatterns = [
    path('', include('simplemooc.core.urls')),
    path('cursos/', include('simplemooc.courses.urls',)),
    path('admin/', admin.site.urls),
]



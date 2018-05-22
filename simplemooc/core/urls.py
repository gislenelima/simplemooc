from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
admin.autodiscover()

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', include(admin.site.urls)),
]
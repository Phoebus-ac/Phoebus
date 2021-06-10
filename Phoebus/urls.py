from django.contrib import admin
from django.conf.urls import handler404
from django.urls import path, include

from Phoebus import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),

    path('api/accounts/', include('accounts.urls')),
    # path('api/manuscripts/', include('manuscripts.urls')),
]

handler404 = views.error404

from rest_framework import routers

from manuscripts import views

default_router = routers.DefaultRouter()

default_router.register('', views.ManuscriptView)

urlpatterns = default_router.urls

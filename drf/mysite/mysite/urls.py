"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MovieViewSet, ActionViewSet, ComedyViewSet
from django.conf.urls.static import static
from django.conf import settings

# # Register the viewset by creating a route
# # this create a url using the router
# router = routers.DefaultRouter()
# # register the MovieViewSet into the router
# router.register('movies', MovieViewSet)

# Register the viewset by creating a route
router = routers.SimpleRouter()
# register the MovieViewSet into the router and with a unique basename
router.register('movies', MovieViewSet, basename='movie')
# # Register url for ActionViewSet and with a unique basename
router.register('action', ActionViewSet, basename='action_movies')
# register url for ComedyViewSet
router.register('comedy', ComedyViewSet, basename='comedy_movies')


urlpatterns = [
    # movies/
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

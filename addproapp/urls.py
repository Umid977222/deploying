from rest_framework import routers
from django.urls import include, path
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.AddViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework')),
    ]

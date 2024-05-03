from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('solicitud/<int:solicitud_id>/cliente',
         views.ClienteBySolicitudAPIView.as_view()),
]

from django.shortcuts import render
from rest_framework import viewsets, generics, status
from django.http import JsonResponse
from rest_framework.response import Response
from .serializer import ClienteSerializer, SolicitudSerializer
from .models import Cliente, Solicitud

# Create your views here.


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer


class ClienteBySolicitudAPIView(generics.RetrieveAPIView):
    serializer_class = ClienteSerializer
    lookup_field = 'solicitud_id'  # Set the lookup field to 'solicitud_id'

    def get_queryset(self):
        solicitud_id = self.kwargs['solicitud_id']
        return Solicitud.objects.filter(pk=solicitud_id)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            instance = queryset.first()
            serializer = self.get_serializer(instance.cliente)
            return Response(serializer.data)
        else:
            return Response({}, status=status.HTTP_200_OK)

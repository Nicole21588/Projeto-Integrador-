from rest_framework import viewsets
from .models import Sensor, Historico, Local, Responsavel, Ambiente
from .serializers import *

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    def get_queryset(self):
        queryset = Sensor.objects.all()
        tipo = self.request.query_params.get('tipo')
        if tipo is not None:
            queryset = queryset.filter(tipo=tipo)
        return queryset

class HistoricoViewSet(viewsets.ModelViewSet):
    queryset = Historico.objects.all().order_by('-timestamp')
    serializer_class = HistoricoSerializer

class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer

class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
from rest_framework import serializers
from .models import Sensor, Historico, Local, Responsavel, Ambiente

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'

class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = '__all__'

class AmbienteSerializer(serializers.ModelSerializer):
    local_nome = serializers.ReadOnlyField(source='local.nome')
    class Meta:
        model = Ambiente
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class HistoricoSerializer(serializers.ModelSerializer):
    sensor_tipo = serializers.ReadOnlyField(source='sensor.tipo')
    class Meta:
        model = Historico
        fields = '__all__'
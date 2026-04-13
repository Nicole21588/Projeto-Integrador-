from django.db import models

class Responsavel(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Local(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Ambiente(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.local} - {self.descricao}"

class Sensor(models.Model):
    TIPO_CHOICES = [
        ('temperatura', 'Temperatura'),
        ('umidade', 'Umidade'),
        ('luminosidade', 'Luminosidade'),
        ('contador', 'Contador'),
    ]
    UNIDADE_CHOICES = [
        ('°C', 'Graus Celsius'),
        ('%', 'Porcentagem'),
        ('lux', 'Lux'),
        ('uni', 'Unidade'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    unidade_medida = models.CharField(max_length=10, choices=UNIDADE_CHOICES)
    mac_address = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    localizacao = models.CharField(max_length=100)
    status_operacional = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tipo} - {self.mac_address}"

class Historico(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor.tipo} - {self.valor} em {self.timestamp}"
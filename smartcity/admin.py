from django.contrib import admin
from .models import Responsavel, Local, Ambiente, Sensor, Historico

admin.site.register(Responsavel)
admin.site.register(Local)
admin.site.register(Ambiente)
admin.site.register(Sensor)
admin.site.register(Historico)
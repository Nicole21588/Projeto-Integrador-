import os
import django
import random
from datetime import datetime, timedelta

# Configura o Django (Obrigatório vir antes dos models)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Agora sim, importa os modelos
from smartcity.models import Sensor, Historico, Local, Responsavel, Ambiente

def popular():
    print("🚀 Iniciando a criação de dados de teste...")
    try:
        # Criar Estrutura Básica
        resp, _ = Responsavel.objects.get_or_create(nome="Coordenação TecnoVille")
        loc, _ = Local.objects.get_or_create(nome="Bloco A - SENAI")
        amb, _ = Ambiente.objects.get_or_create(local=loc, responsavel=resp, descricao="Laboratório de IoT")

        tipos = [
            ('temperatura', '°C'),
            ('umidade', '%'),
            ('luminosidade', 'lux'),
            ('contador', 'uni')
        ]

        for tipo, unidade in tipos:
            # Criar Sensor
            sensor, _ = Sensor.objects.get_or_create(
                tipo=tipo,
                unidade_medida=unidade,
                mac_address=f"00:11:22:AA:BB:{random.randint(10,99)}",
                latitude=-23.5,
                longitude=-46.6,
                localizacao="Poste Principal",
                status_operacional=True
            )

            # Criar 5 registros de histórico
            for i in range(5):
                Historico.objects.create(
                    sensor=sensor,
                    valor=round(random.uniform(20.0, 40.0), 2),
                    timestamp=datetime.now() - timedelta(hours=i)
                )
        
        print("✅ SUCESSO! Banco populado com sucesso.")
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == '__main__':
    popular()
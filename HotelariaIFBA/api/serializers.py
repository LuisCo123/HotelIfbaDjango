from rest_framework import serializers
from HotelariaIFBA import models

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = '__all__'
class ListaDeServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ListaDeServico
        fields = '__all__'
class TipoServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoServico
        fields = '__all__'
class EmpregadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = '__all__'
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reserva
        fields = '__all__'
class AlojamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alojamento
        fields = '__all__'
class ServicosUtilizadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServicosUtilizados
        fields = '__all__'
# Empresa, ListaDeServico, TipoServico,Empregados,Cliente,Reserva,Alojamento,ServicosUtilizados
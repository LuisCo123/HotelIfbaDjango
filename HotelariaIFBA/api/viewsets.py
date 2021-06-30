from rest_framework import viewsets
from HotelariaIFBA.api import serializers
from HotelariaIFBA import models
# Empresa, ListaDeServico, TipoServico,Empregados,Cliente,Reserva,Alojamento,ServicosUtilizados
class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpresaSerializer
    queryset = models.Empresa.objects.all()

class ListaDeServicoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ListaDeServicoSerializer
    queryset = models.ListaDeServico.objects.all()

class TipoServicoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TipoServicoSerializer
    queryset = models.TipoServico.objects.all()

class EmpregadosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpregadosSerializer
    queryset = models.Empregados.objects.all()

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()

class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReservaSerializer
    queryset = models.Reserva.objects.all()

class AlojamentoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AlojamentoSerializer
    queryset = models.Alojamento.objects.all()

class ServicosUtilizadosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ServicosUtilizadosSerializer
    queryset = models.ServicosUtilizados.objects.all()
from django.db.models import query
from rest_framework import viewsets
from HotelariaIFBA.api import serializers
from HotelariaIFBA import models
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
# Empresa, ListaDeServico, TipoServico,Empregados,Cliente,Reserva,Alojamento,ServicosUtilizados
class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpresaSerializer
    queryset = models.Empresa.objects.all()
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)  
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    def get_queryset(self):
        username = self.request.query_params.get('username')
        if username is not None:
            self.queryset = User.objects.filter(username=username)
        return self.queryset
class ListaDeServicoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ListaDeServicoSerializer
    queryset = models.ListaDeServico.objects.all()
    def get_queryset(self):
        empresaid = self.request.query_params.get('empresa')
        servicoid = self.request.query_params.get('servico')
        if servicoid is not None:
            self.queryset = models.ListaDeServico.objects.filter(servico=servicoid)
        if empresaid is not None:
            self.queryset = models.ListaDeServico.objects.filter(empresa=empresaid)
        if empresaid is not None and servicoid is not None:
            self.queryset = models.ListaDeServico.objects.filter(empresa=empresaid,servico=servicoid)
        return self.queryset

class TipoServicoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TipoServicoSerializer
    queryset = models.TipoServico.objects.all()

class EmpregadosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpregadosSerializer
    queryset = models.Empregados.objects.all()

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()
    def get_queryset(self):
        username = self.request.query_params.get('user')
        if username is not None:
            self.queryset = models.Cliente.objects.filter(user=username)
        return self.queryset

class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReservaSerializer
    queryset = models.Reserva.objects.all()
    def get_queryset(self):
        clienteid = self.request.query_params.get('cliente')
        if clienteid is not None:
            self.queryset = models.Reserva.objects.filter(cliente=clienteid)
        return self.queryset

class AlojamentoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AlojamentoSerializer
    queryset = models.Alojamento.objects.all()
    def get_queryset(self):
        empresaid = self.request.query_params.get('empresa')
        if empresaid is not None:
            self.queryset = models.Alojamento.objects.filter(empresa=empresaid)
        return self.queryset

class ServicosUtilizadosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ServicosUtilizadosSerializer
    queryset = models.ServicosUtilizados.objects.all()
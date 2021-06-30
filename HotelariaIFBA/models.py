from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

TYPE_STATUS = (
    ('Reservado','Reservado'),
    ('Finalizado', 'Finalizado'),
    ('Em andamento', 'Em andamento'),
    ('Cancelado', 'Cancelado'),
)
TYPE_HOTELS = (
    ('Hotel','Hotel'),
    ('Pousada', 'Pousada'),
    ('Sitio', 'Sitio'),
    ('Hostel', 'Hostel'),
)
TYPE_STATUS_ALOJAMENTO = (
    ('Disponivel','Disponivel'),
    ('Indisponivel', 'Indisponivel'),
)
TYPE_PERIODO = (
    ('Temporada','Temporada'),
    ('Fora Temporada', 'Fora Temporada'),
)
TYPE_FORMA_PAGAMENTO = (
    ('Cartao_Debito','Cartao_Debito'),
    ('Cartao_Credito', 'Cartao_Credito'),
    ('A Vista', 'A Vista'),
    ('Cheque', 'Cheque'),
)
class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=90)
    telefone = models.IntegerField()
    categoria = models.CharField( max_length=30, choices=TYPE_HOTELS)
    email = models.CharField(max_length=60)

    def __str__(self):
        return self.nome

class Empregados(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    funcao = models.CharField(max_length=30)
    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class TipoServico(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=60)
    preco = models.IntegerField()
    numPessoas = models.IntegerField()
    periodo = models.CharField( max_length=30, choices=TYPE_PERIODO)

    def __str__(self):
        return self.nome

class ListaDeServico(models.Model):
    servico = models.ForeignKey(TipoServico, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    def __str__(self): 
        return "%s"%self.servico
class Alojamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    numero = models.IntegerField()
    capacidade = models.IntegerField()
    status = models.CharField( max_length=30, choices=TYPE_STATUS_ALOJAMENTO)
    diaria = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return "%s"%self.numero

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    nacionalidade = models.CharField( max_length=50)
    dataDeNascimento = models.DateField()
    endereco = models.CharField(max_length=60)
    telefone = models.IntegerField()
    rg = models.IntegerField()
    dataRG = models.DateField()
    email = models.CharField(max_length=60,blank=True, null=True)
    numeroCartao = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if(self.pk is None):
            if( self.email != ""):
                new_password = User.objects.make_random_password()
                self.usuario = User.objects.create_user(username=self.nome, email=self.email, password=new_password)
                try:
                    send_mail(
                    'Subject here',
                    'sua senha da hotelaria ifba é :' + new_password,
                    'HotelIFBATeste@gmail.com',
                    [self.email],
                    fail_silently=False,
                )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                
            else:
                self.usario = User.objects.create_user(username=self.nome, email=self.email, password=self.nome+"12345678")
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.nome 


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    alojamento = models.ForeignKey(Alojamento, on_delete=models.CASCADE)
    listaDeServico = models.ForeignKey(ListaDeServico, on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    formaDePagamento = models.CharField( max_length=30, choices=TYPE_FORMA_PAGAMENTO)
    status = models.CharField( max_length=30, choices=TYPE_STATUS)

    def __str__(self):
        return "Cliente: %s" % self.cliente + "Alojamento: %s"%self.alojamento

class ServicosUtilizados(models.Model):
    servico = models.ForeignKey(ListaDeServico, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)


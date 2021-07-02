from django.conf import settings
from django.db import models
from django.db.models.fields import related
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
    empresa = models.CharField(max_length=30)
    endereco = models.CharField(max_length=90)
    telefone = models.IntegerField()
    categoria = models.CharField( max_length=30, choices=TYPE_HOTELS)
    email = models.CharField(max_length=60)

    def __str__(self):
        return self.empresa

class Empregados(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    funcao = models.CharField(max_length=30)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class TipoServico(models.Model):
    servico = models.CharField(max_length=30,)
    descricao = models.CharField(max_length=60)
    preco = models.FloatField()
    numPessoas = models.IntegerField()
    periodo = models.CharField( max_length=30, choices=TYPE_PERIODO)

    def __str__(self):
        return self.servico

class ListaDeServico(models.Model):
    servico = models.ForeignKey(TipoServico,on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    def __str__(self): 
        return "%s"%self.pk
class Alojamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    alojamento = models.IntegerField()
    capacidade = models.IntegerField()
    descricao = models.CharField( max_length=30)
    status = models.CharField( max_length=30, choices=TYPE_STATUS_ALOJAMENTO)
    diaria = models.FloatField(blank=True, null=True)
    foto = models.FileField(blank=True, null=True, upload_to="HotelariaIFBA/roomImages/")
    def __str__(self):
        return "%s"%self.alojamento

class Cliente(models.Model):
    cliente = models.CharField(max_length=30)
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
                self.usuario = User.objects.create_user(username=self.cliente, email=self.email, password=new_password)
                try:
                    send_mail(
                    'Olá ' + self.cliente,
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
        return self.cliente 


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    alojamento = models.ForeignKey(Alojamento, on_delete=models.CASCADE)
    servico = models.ForeignKey(ListaDeServico, on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    formaDePagamento = models.CharField( max_length=30, choices=TYPE_FORMA_PAGAMENTO)
    status = models.CharField( max_length=30, choices=TYPE_STATUS)

    def __str__(self):
        return "Cliente: %s" % self.cliente + " Alojamento: %s"%self.alojamento

class ServicosUtilizados(models.Model):
    servico = models.ForeignKey(ListaDeServico, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    data = models.DateField()

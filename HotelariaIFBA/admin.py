from django.contrib import admin
from .models import *
from rangefilter.filters import DateRangeFilter
admin.site.register({ Alojamento, Empresa, ListaDeServico, TipoServico,Empregados})
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'rg')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id','cliente', 'alojamento', 'dataInicio', 'dataFim', 'status')
    list_filter = (('dataInicio',  DateRangeFilter),('dataFim',  DateRangeFilter),("status"),)


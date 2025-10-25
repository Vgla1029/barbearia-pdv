from django.contrib import admin
from .models import Cliente, Servico, Agendamento

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Servico)
admin.site.register(Agendamento)

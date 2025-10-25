from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome if self.nome else "Cliente sem nome"

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome if self.nome else "Serviço sem nome"

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=True, blank=True)
    data_hora = models.DateTimeField()

    def __str__(self):
        cliente_nome = self.cliente.nome if self.cliente else "Cliente removido"
        servico_nome = self.servico.nome if self.servico else "Serviço removido"
        return f"{cliente_nome} - {servico_nome} em {self.data_hora}"
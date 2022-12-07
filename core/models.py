from django.db import models
from django.contrib.auth.models import AbstractUser

class Mercado(models.Model):
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    avaliacao = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50, blank= True, null=True)
    quantidade = models.IntegerField(null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    mercado = models.ForeignKey(
        Mercado, on_delete=models.PROTECT, related_name="produtos", null=True, blank=True
    )

    def __str__(self):
        return self.nome

class Lista(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="+", blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.descricao})"
    
class Usuario(AbstractUser):
     data_nascimento = models.DateField(blank=True, null=True)
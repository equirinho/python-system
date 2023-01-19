from django.db import models
from uuid import uuid4

# Create your models here.

class Cadastro(models.Model):
    nome= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    endereco_usuario= models.CharField(max_length=100)
    pais= models.CharField(max_length=15)
    estado= models.CharField(max_length=20)
    municipio= models.CharField(max_length=40)
    cep= models.CharField(max_length=8)
    rua= models.CharField(max_length=40)
    numero= mmodels.CharField(max_length=4)
    complemento = models.CharField(max_length=100)
    cpf= models.CharField(max_length=11)  
    pis= models.CharField(max_length=11)
    senha= models.CharField(max_length=15)  










#     nome
# ○ email
# ○ endereço do usuário
# ■ País
# ■ Estado
# ■ Município
# ■ CEP
# ■ Rua
# ■ Número
# ■ Complemento
# ○ CPF
# ○ PIS
# ○ Senha

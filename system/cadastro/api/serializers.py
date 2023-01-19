from rest_framework import serializers
from cadastro import models

class CadastroSerializer(serializers.ModelSerializer):
    class Meta: #meta é uma classe interna que recebe 2 parâmetros: model e fields
        model=models.Cadastro
        fields='__all__' #quero trazer todos os campos do meu model, são os campos desse serializr
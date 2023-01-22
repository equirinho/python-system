from rest_framework import viewsets
from cadastro.api import serializers
from cadastro import models
from rest_framework.permissions import IsAuthenticated

class CadastroViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)

    serializer_class = serializers.CadastroSerializer
    queryset = models.Cadastro.objects.all()  #todos os campos do nosso modelo

